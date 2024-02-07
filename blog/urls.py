from . import views
from django.urls import path

urlpatterns = [
    path('about/', views.about, name='about_urls'),
    path('contact/', views.contact, name='contact_urls'),
    path('index/', views.index, name='index_urls'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('delete/<int:comment_id>/', views.CommentDelete.as_view(), name='delete_comment'),
    path('edit/<int:comment_id>/', views.CommentEdit.as_view(), name='edit_comment'),
    path("", views.PostList.as_view(), name="blog"),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('search-blogs/', views.BlogSearchView.as_view(), name="search_blogs")
]