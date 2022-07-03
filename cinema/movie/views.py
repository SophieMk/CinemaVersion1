from django.shortcuts import render
from .models import Movie

# Create your views here.


def allFilms(request):
   movies = Movie.objects.all()
   return render(request, 'ListOfFilms.html', {'movies': movies})

def player(request, film_id):
   return render(request, 'player.html', {'film_id': film_id})

