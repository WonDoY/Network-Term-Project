#urls.py
from django.conf.urls import include, url
#import ./views
from . import views
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home', views.home),
    url(r'^game', views.game),
    url(r'^admin', admin.site.urls),
    # /path = r'^blah', views.blah
]

# urls.py는 주소와 장고의 뷰를 연결 해 주는 역을 합니다.할
#여기서 중요한 부분은 urlpatterns입니다. patterns는 두 번째 인자부터 url(패턴, 뷰)를 인자로 받습니다. 주소가 이 패턴에 걸리게 되면 해당하는 뷰를 호출 하라는 의미입니다. 패턴은 정규표현식으로 이루어져 있습니다. 패턴 뒤에 뷰 대신 다른 urls.py가 오게 되면 해당하는 urls.py에서 URL을 받아서 처리하게 됩니다.
#ex) r'^main/$' -> http://127.0.0.1:8000/main


#ex) 만약 http://127.0.0.1:8000/suspect/man/ 으로 접속할 때 man에 대한 페이지가 나오고 http://127.0.0.1:8000/suspect/women/ 로 접속하면 women에 대한 정보가 나오게 하려면 정규표현식을 이용하여 인자를 만들어야 합니다. 


#r'^suspect/(?P<suspect>\w+)/$' 와 같이 패턴을 만든다면 뷰의 suspect라는 인자에 \w+에 해당하는 값이 전달 될 것입니다. 만약 http://127.0.0.1:8000/suspect/man/ 로 접속을 한다면 man으로 전달되겠습니다. 
