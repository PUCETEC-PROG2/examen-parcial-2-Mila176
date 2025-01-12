from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies_list.html', {'movies': movies})

def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/detail.html', {'movie': movie})