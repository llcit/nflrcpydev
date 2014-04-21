from django.conf.urls import *

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('django.contrib.flatpages.views',
    # FLATPAGES Experiment
    url(r'^publications/khmer/$', 'flatpage', {'url': '/publications/khmer/'}, name='Khmer'),
    url(r'^publications/filipino/$', 'flatpage', {'url': '/publications/filipino/'}, name='Filipino'),
    url(r'^publications/aozora/$', 'flatpage', {'url': '/publications/aozora/'}, name='Aozora'),
)

urlpatterns += patterns('nflrcapp.views',
    # LEVEL 2 PAGES (/level-2-pages)
    url(r'^about/$', 'about', name='about'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^contact/view/(.*)$', 'contactview', name='contactview'),
    url(r'^languages/(.*)$', 'languages', name='languages'),
    url(r'^outreach/$', 'home', name='home'),
    url(r'^prodev/view/(.*)$', 'prodevview', name='prodevview'),
    url(r'^prodev/(.*)$', 'prodev', name='prodev'),
    url(r'^projects/view/(.*)$', 'projectview', name='projectview'),
    url(r'^projects/(.*)$', 'projects', name='projects'),
    url(r'^publications/view/(.*)$', 'pubview', name='pubview'),
    url(r'^publications/(.*)$', 'publications', name='publications'),
    url(r'^resources/(.*)$', 'resources', name='resources'),
    url(r'^search/(.*)$', 'search', name='search'),
    url(r'^software/(.*)$', 'software', name='software'),
    url(r'^story/(.*)$', 'storyview', name='story'),
    url(r'^workshops-conferences/$', 'workshop_conf', name='confs'),
    
    # LEVEL 1 (root)
    url(r'^$', 'home'),
    
    
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



