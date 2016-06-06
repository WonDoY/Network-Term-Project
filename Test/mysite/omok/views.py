from django.shortcuts import render
from .models import Omok
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request, 'omok/home.html')

def game(request):
	
	return render(request, 'omok/game.html')



#먼저 HttpResponse라는 객체를 사용하기 위해 django.http에 있는
# HttpResponse 객체를 import 하였고, HttpResponse는 사용자가 서버
#에 접속 했을 때 서버에서 사용자에게 보내주는 응답을 담는 객체입니
#다. HttpResponse를 통해 html 소스 등을 리턴 해 주면 사용자 브라우
#저에 그 내용이 그대로 뜨게 됩니다.

