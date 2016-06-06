#urls.py
from django.conf.urls import include, url
#import ./views
from . import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index', views.index),
    url(r'^game', views.game),
    # /path = r'^blah', views.blah
]
