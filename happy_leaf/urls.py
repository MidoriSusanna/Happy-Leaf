from django.contrib import admin
from django.urls import path, include
from blog.views import index, about, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name='blog_urls'),
    path("accounts/", include("allauth.urls")),
    path('about/', about, name='about_urls'),
    path('index/', index, name='index_urls'),
    path('contact/', contact, name='contact_urls'),
]
