#urls.py
from django.conf.urls import include, url
#load ./views
from . import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index)
    url(r'^admin/', include(admin.site.urls)),
]
