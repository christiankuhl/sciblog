from django.conf.urls import url
from blog.models import Post
from django.views.generic import ListView, DetailView
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import PostSitemap, FlatpageSitemap
from blog.views import PostsFeed, getSearchResults, MathematicalToyView, PostListView
from django.contrib.flatpages.models import FlatPage

# Define sitemaps
sitemaps = {
    'posts': PostSitemap,
    'pages': FlatpageSitemap
}

urlpatterns = [
    # Index
    url(r'^(?P<page>\d+)?/?$', PostListView.as_view(), name='index'),
    # Individual posts
    url(r'^blog/(?P<pub_date__year>\d{4})/(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(model=Post,), name='post'),
    # Post RSS feed
    url(r'^feed/posts/$', PostsFeed()),
    # Search posts
    url(r'^search', getSearchResults, name='search'),
    #robots.txt
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /admin/", content_type="text/plain")),
    #sitemap
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # Math toys
    url(r'^mandelbrot', MathematicalToyView("mandelbrot.html")),
    url(r'^vortices', MathematicalToyView("vortices.html")),
    # Flat pages
    url(r'^<page>$', DetailView.as_view(model=FlatPage,), name="flatpage"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
