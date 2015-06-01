from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wikicoding.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

#################################################
# For requests to / and /wiki/			#
# Immediately isssue HTTP 301 Moved Permanently #
# to /wiki/Main_Page				#
#################################################

urlpatterns += patterns('',
    url(r'^$', RedirectView.as_view(url='/wiki/Main_Page/', permanent=True), name='get'),
    url(r'^wiki/$', RedirectView.as_view(url='/wiki/Main_Page/', permanent=True), name='get'),
    url(r'^wiki/_/(?P<remainder>[^/]+/)$',
        RedirectView.as_view(url='/wiki/%(remainder)s', query_string=True, permanent=True), name='get'),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/wiki/Main_Page/', permanent=True), name='get'),
)

from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern
urlpatterns += patterns('',
    # (r'^notifications/', get_nyt_pattern()),
    (r'', get_wiki_pattern())
)
