
from django.conf.urls import url, patterns, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from filebrowser.sites import site

from .views import SearchHaystackView, prodev_update_view, pub_update_view, project_update_view, story_update_view
from .models import NflrcNewsFeed

from badge_site.views import (
    IndexView, BadgeClaimView, BadgeClaimCodeView, SendAwardNotificationView,
    IssuerCreateView, IssuerUpdateView, IssuerListView,
    BadgeCreateView, BadgeUpdateView, BadgeListView,
    AwardCreateView, AwardUpdateView, AwardListView
)


urlpatterns = patterns('',
    # Handle cfm requests from the wild.
    url(r'^get_publication\.cfm$', 'nflrcapp.views.cfm_publication_handler', name='cfm_publication_handler'),
    url(r'^searchsite_pub\.cfm$', 'nflrcapp.views.cfm_searchsite_handler', name='cfm_searchsite_handler'),
    url(r'^get_project\.cfm$', 'nflrcapp.views.cfm_project_handler', name='cfm_project_handler'),
    url(r'^(?P<cfmtoken>.*)\.cfm/$', 'nflrcapp.views.cfm_global_handler', name='cfm_global_handler'),

    # SECURE FILE HANDLER
    url(r'^nflrcPRIVATE/(?P<f>.*)$', 'nflrcapp.views.nflrcprivate', name='download'),

    # BADGE SERVER
    url(r'^badgefarm/$', IndexView.as_view(), name='badge_home'),

    url(r'^badgefarm/issuer/add/$', IssuerCreateView.as_view(), name='create_issuer'),
    url(r'^badgefarm/issuer/edit/(?P<pk>\d+)/$', IssuerUpdateView.as_view(), name='edit_issuer'),
    url(r'^badgefarm/issuers/$', IssuerListView.as_view(), name='list_issuers'),

    url(r'^badgefarm/badge/add/(?P<issuer>\d+)/$', BadgeCreateView.as_view(), name='create_badge_by_issuer'),
    url(r'^badgefarm/badge/edit/(?P<pk>\d+)/$', BadgeUpdateView.as_view(), name='edit_badge'),
    url(r'^badgefarm/badges/$', BadgeListView.as_view(), name='list_badges'),

    url(r'^badgefarm/award/add/(?P<badge>\d+)/$', AwardCreateView.as_view(), name='create_award_by_badge'),
    url(r'^badgefarm/award/edit/(?P<pk>\d+)/$', AwardUpdateView.as_view(), name='edit_award'),
    # url(r'^award/delete/(?P<pk>\d+)/$', DeleteAwardView.as_view(), name='delete_award'),
    # url(r'^award/revoke/(?P<award_to_revoke>\d+)/$', RevokeAwardView.as_view(), name='revoke_award'),
    url(r'^badgefarm/awards/$', AwardListView.as_view(), name='list_awards'),
    url(r'^badgefarm/awards/(?P<pk>\d+)/$', AwardListView.as_view(), name='list_awards_by_badge'),

    url(r'^badgefarm/claim/$', BadgeClaimView.as_view(), name='claim_badge'),
    url(r'^badgefarm/claim/(?P<claim_code>\w+)/$', BadgeClaimCodeView.as_view(), name='claim_badge_with_code'),
    url(r'^badgefarm/notify/(?P<pk>\d+)/$', SendAwardNotificationView.as_view(), name='send_award_email'),


    # LEVEL 2 PAGES (/level-2-pages)

    url(r'^staffdocs/$', 'nflrcapp.views.staffdocs', name='staffdocs_index'),
    url(r'^staffdocs/view/(?P<item>\d+)/$', 'nflrcapp.views.privateview', name='staffdocsview'),

    url(r'^about/$', 'nflrcapp.views.about', name='about_index'),
    url(r'^about/update/(?P<pk>\d+)/$', story_update_view.as_view(), name='story_update_view'),
    url(r'^about/(?P<item>\d+)/$', 'nflrcapp.views.aboutview', name='aboutview'),


    url(r'^contact/$', 'nflrcapp.views.contact', name='contact_index'),
    url(r'^contact/view/(?P<person>\d+)/$', 'nflrcapp.views.contactview', name='contactview'),

    url(r'^events/view/(?P<item>[-\w]+)/$', 'nflrcapp.views.prodevview', name='eventview'),
    url(r'^events/update/(?P<pk>\d+)/$', prodev_update_view.as_view(), name='event_update_view'),
    url(r'^events/(?P<tag>[-\w]+)/$', 'nflrcapp.views.prodev', name='events'),
    url(r'^events/$', 'nflrcapp.views.prodev', name='events_index'),
    

    url(r'^languages/(?P<tag>[-\w]+)/$', 'nflrcapp.views.languages', name='languages'),
    url(r'^languages/$', 'nflrcapp.views.languages', name='languages_index'),

    url(r'^newswire/$', NflrcNewsFeed(), name='news-wire'),

    url(r'^projects/view/(?P<item>[-\w]+)/$', 'nflrcapp.views.projectview', name='projectview'),
    url(r'^projects/update/(?P<pk>\d+)/$', project_update_view.as_view(), name='project_update_view'),
    url(r'^projects/(?P<tag>[-\w]+)/$', 'nflrcapp.views.projects', name='projects'),
    url(r'^projects/$', 'nflrcapp.views.projects', name='projects_index'),

    url(r'^publications/view/(?P<item>[-\w]+)/$', 'nflrcapp.views.pubview', name='pubview'),
    url(r'^publications/update/(?P<pk>\d+)/$', pub_update_view.as_view(), name='pub_update_view'),
    url(r'^publications/(?P<tag>[-\w]+)/$', 'nflrcapp.views.publications', name='publications'),
    url(r'^publications/$', 'nflrcapp.views.publications', name='publications_index'),

    # Prototype index -- temporary --
    url(r'^prototype/$', 'nflrcapp.views.home_prototype', name='proto'),

    # Prototype admin (curator) ui -- temporary --  
    url(r'^admin/curator/$', 'nflrcapp.views.curator_view', name='curator'),
    url(r'^admin/curator/update_rank/$', 'nflrcapp.views.curator_update_rank_view', name='curator_update_rank'),
    url(r'^admin/curator/update_feature_rank/$', 'nflrcapp.views.curator_update_featured_rank_view', name='curator_update_feature_rank'),

    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls), name='adminsite'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^search/', SearchHaystackView.as_view(), name='search_haystack'),
    # deprecated in favor of haystack indexing:
    # url(r'^find/$', 'nflrcapp.views.search', name='search'),

    # Filter site objects by tag. Must be last so that previous url patterns are caught first!
    url(r'^([-\w]+)/$', 'nflrcapp.views.site_filter', name='site_filter'),


    # LEVEL 1 (root)
    url(r'^$', 'nflrcapp.views.home', name='homestead'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



