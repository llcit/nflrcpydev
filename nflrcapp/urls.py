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

    url(r'^about/$', 'about', name='about_index'),
    url(r'^about/(?P<item>\d+)/$', 'aboutview', name='aboutview'),

    url(r'^contact/$', 'contact', name='contact_index'),
    url(r'^contact/view/(?P<person>\d+)/$', 'contactview', name='contactview'),

    url(r'^events/view/(?P<item>[-\w]+)/$', 'prodevview', name='eventview'),
    url(r'^events/(?P<tag>[-\w]+)/$', 'prodev', name='events'),
    url(r'^events/$', 'prodev', name='events_index'),

    url(r'^find/$', 'search', name='search'),
   
    url(r'^languages/(?P<tag>[-\w]+)/$', 'languages', name='languages'),
    url(r'^languages/$', 'languages', name='languages_index'),
    
    url(r'^newswire/$', NflrcNewsFeed(), name='news-wire'),

    url(r'^projects/view/(?P<item>[-\w]+)/$', 'projectview', name='projectview'),
    url(r'^projects/(?P<tag>[-\w]+)/$', 'projects', name='projects'),
    url(r'^projects/$', 'projects', name='projects_index'),

    url(r'^publications/view/(?P<item>[-\w]+)/$', 'pubview', name='pubview'),
    url(r'^publications/(?P<tag>[-\w]+)/$', 'publications', name='publications'),
    url(r'^publications/$', 'publications', name='publications_index'),
  
    # Prototype index -- temporary --
    url(r'^prototype/$', 'home_prototype', name='proto'),


    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

	url(r'^search/', include('haystack.urls')),

    # Filter site objects by tag. Must be last so that previous url patterns are caught first!
    url(r'^([-\w]+)/$', 'site_filter', name='site_filter'),


    # LEVEL 1 (root)
    url(r'^$', 'home'),
    
    
    


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



