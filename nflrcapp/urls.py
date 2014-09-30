from django.conf.urls import *

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from filebrowser.sites import site

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
   
    url(r'^languages/(.*)$', 'languages', name='languages'),

    url(r'^projects/view/(.*)$', 'projectview', name='projectview'),
    url(r'^projects/(.*)$', 'projects', name='projects'),

    url(r'^publications/view/(.*)$', 'pubview', name='pubview'),
    url(r'^publications/(.*)$', 'publications', name='publications'),

    # url(r'^stories/$', 'stories', name='stories'),
    # url(r'^story/(.*)$', 'storyview', name='story'),
    
    
    # Prototype index -- temporary --
    url(r'^prototype/$', 'home_prototype', name='proto'),

    # LEVEL 1 (root)
    url(r'^$', 'home'),
    
    
    # url(r'^search/', include('haystack.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



