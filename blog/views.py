from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Post
from .models import Comment
from .forms import CommentForm


class PostList(generic.ListView):
    """Render a list of published posts"""
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 6


class PostDetail(View):
    """Render details of a specific post"""
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class CommentDelete(View):
    """View to delete a comment"""
    def get(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)
        return render(request, "comment_delete.html", {"comment": comment})

    def post(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)

        if request.user.is_superuser or request.user.username == comment.name:
            if request.POST.get("confirm_delete"):
                comment.delete()
            messages.success(request,
                             "You have successfully deleted the comment.")
            return HttpResponseRedirect(reverse('post_detail',
                                        args=[comment.post.slug]))
        else:
            messages.error(request, "You do not have"
                           "permission to delete this comment.")
            return HttpResponseRedirect(reverse('post_detail',
                                        args=[comment.post.slug]))


class CommentEdit(View):
    """View to edit a comment"""
    def get(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)
        form = CommentForm(instance=comment)
        return render(
            request,
            "comment_edit.html",
            {
                "comment": comment,
                "form": form,
            }
        )

    def post(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "You have successfully updated the comment.")
            return HttpResponseRedirect(reverse('post_detail',
                                        args=[comment.post.slug]))
        else:
            messages.error(request, "Error updating the comment."
                           "Please check the form.")
            return render(
                request,
                "comment_edit.html",
                {
                    "comment": comment,
                    "form": form,
                }
            )


class PostLike(View):
    """View to handle post likes"""
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class BlogSearchView(generic.ListView):
    """View to handle blog post searching"""
    model = Post
    template_name = 'blog.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Post.objects.filter(
                Q(title__icontains=query) | Q(category__name__icontains=query)
                ).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get("q", "")
        return context


def index(request):
    """Render the index page"""
    return render(request, "index.html")


def about(request):
    """Render the about page"""
    return render(request, "about.html")


def contact(request):
    """Render the contact page"""
    return render(request, "contact.html")
