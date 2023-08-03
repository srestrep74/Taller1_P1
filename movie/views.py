from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {
        'name' : 'Sebastian Restrepo'
    }
    return render(request, 'home.html', context)
