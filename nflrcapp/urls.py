from django.conf.urls import url, patterns, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from filebrowser.sites import site

from .models import NflrcNewsFeed

urlpatterns = patterns('django.contrib.flatpages.views',
    # FLATPAGES Experiment
    url(r'^publications/khmer/$', 'flatpage', {'url': '/publications/khmer/'}, name='Khmer'),
    url(r'^publications/filipino/$', 'flatpage', {'url': '/publications/filipino/'}, name='Filipino'),
    url(r'^publications/aozora/$', 'flatpage', {'url': '/publications/aozora/'}, name='Aozora'),
)

urlpatterns += patterns('nflrcapp.views',
    
    # LEVEL 2 PAGES (/level-2-pages)

    
    url(r'^about/$', 'about', name='about'),
    url(r'^about/(.*)$', 'aboutview', name='aboutview'),

    url(r'^contact/$', 'contact', name='contact'),
    url(r'^contact/view/(.*)$', 'contactview', name='contactview'),

    url(r'^events/view/(.*)$', 'prodevview', name='prodevview'),
    url(r'^events/(.*)$', 'prodev', name='confs'),

    url(r'^find/$', 'search', name='search'),
   
    url(r'^languages/(.*)/$', 'languages', name='languages'),

    url(r'^newswire/$', NflrcNewsFeed(), name='news-wire'),

    url(r'^projects/view/(.*)/$', 'projectview', name='projectview'),
    url(r'^projects/(.*)$', 'projects', name='projects'),

    url(r'^publications/view/(.*)/$', 'pubview', name='pubview'),
    url(r'^publications/(.*)$', 'publications', name='publications'),

    # url(r'^stories/$', 'stories', name='stories'),
    # url(r'^story/(.*)$', 'storyview', name='story'),
    
    
    # Prototype index -- temporary --
    url(r'^prototype/$', 'home_prototype', name='proto'),


    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Filter site objects by tag. Must be last so that previous url patterns are caught first!
    url(r'^([-\w]+)/$', 'site_filter', name='site_filter'),

    # LEVEL 1 (root)
    url(r'^$', 'home'),
    
    
    # url(r'^search/', include('haystack.urls')),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



