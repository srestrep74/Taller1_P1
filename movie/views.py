from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    context = {
        'searchTerm' : searchTerm,
        'movies' : movies
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')
