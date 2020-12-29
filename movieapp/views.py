from django.shortcuts import render
#import models
from .models import Movie

# Create your views here.
def index(request):
    #Declarate movie dta import
    movie_data = Movie.objects.all()
    return render(request, 'index.html', {"movie": movie_data})

def testimonial(request):
    return render(request, 'testimonial.html', {})

def movie(request, movie_id):
    movie_data = Movie.objects.get(id=movie_id)
    return render (request, 'movie.html', {"movie": movie_data})