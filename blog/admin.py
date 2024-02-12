from django.contrib import admin
from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


# Create the Admin Panel - Post section
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """Admin view for Post"""
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Create the Admin Panel - Comment section
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin view for Comment"""
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    # Comments need to be approved before appearing on the website
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """Approve selected comments"""
        queryset.update(approved=True)


# Create the Admin Panel - Category section
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin view for Category"""
    list_display = ('name',)
    search_fields = ('name',)
