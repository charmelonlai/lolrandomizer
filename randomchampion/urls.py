from django.conf.urls import patterns, include, url
from randomchampion.champdatabase.views import FrontPageView,JungleView,TopView,MidView,ADView,SupportView
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'randomchampion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
url(r'^admin/', include(admin.site.urls)),
url(r'^$',
    	FrontPageView.as_view(),
    	name='frontpage'),
url(r'^all/', FrontPageView.as_view()),
url(r'^jungler/', JungleView.as_view()),
url(r'^top/', TopView.as_view()),
url(r'^mid/', MidView.as_view()),
url(r'^marksman/', ADView.as_view()),
url(r'^support/', SupportView.as_view()),
url(r'^splash/(?P<path>.*)$', 'django.views.static.serve',
{'document_root': settings.MEDIA_ROOT}),
)
