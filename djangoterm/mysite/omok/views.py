from django.shortcuts import render
from .models import Omok
# Create your views here.
def index(request):
	return render(request, 'omok/index.html')

def game(request):

	omok = Omok()
	omok.play()
	return render(request, 'omok/game.html')