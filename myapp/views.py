from django.shortcuts import render
from models import Car

# Create your views here.
def carlist(request):
	mylist=[{'model':i.model,'color':i.color} for i in Car.objects.all()]
	return render(request, 'carlist.html', {'mylist':mylist})
