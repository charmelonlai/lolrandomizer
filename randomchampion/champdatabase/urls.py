from django.conf.urls import patterns, include, url
# App Views
from randomchampion.champdatabase.views import FrontPageView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eatwithus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', FrontPageView.as_view()),
)