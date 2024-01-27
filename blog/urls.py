from . import views
from django.urls import path

urlpatterns = [
    path('about/', views.about, name='about_urls'),
    path('contact/', views.contact, name='contact_urls'),
    path('index/', views.index, name='index_urls'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('delete/<int:comment_id>/', views.PostDetail.as_view(), name='delete_comment'),
    path("", views.PostList.as_view(), name="blog"),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]