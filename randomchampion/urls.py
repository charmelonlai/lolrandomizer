from django.conf.urls import patterns, include, url
from randomchampion.champdatabase.views import FrontPageView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'randomchampion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', FrontPageView.as_view()),
)
