from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # omok
    url(r'^', include('omok.urls')),
    
    #localhost:8000으로 요청이 들어오면 omok.urls로 전달
    url(r'^admin/', include(admin.site.urls)),
]
