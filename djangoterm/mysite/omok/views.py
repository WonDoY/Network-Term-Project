from django.shortcuts import render
from .models import Omok
# Create your views here.
def home(request):
	return render(request, 'omok/home.html')

def game(request):

	omok = Omok()
	context ={'locate' : omok.locateString() }
	
	return render(request, 'omok/game.html',context)