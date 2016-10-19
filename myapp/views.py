from django.shortcuts import render

# Create your views here.
def carlist(request):
	return render(request, 'carlist.html', {})
