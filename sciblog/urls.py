from django.conf.urls import include, url
from django.contrib import admin
import django

# app_name = "sciblog"

urlpatterns = [
        url(r'^', include('blog.urls')),
        url(r'^admin/', admin.site.urls),
        url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    ]
