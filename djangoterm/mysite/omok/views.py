from django.shortcuts import render
from .models import Omok
# Create your views here.
def home(request):
	return render(request, 'omok/home.html')

def game(request):

	omok = Omok()
	st = ""
	for x in range(13):
		for y in range(13):
			st += "{}".format((omok.locate[x][y]))
		st += '<br>'
	
	return httpResponse(st)