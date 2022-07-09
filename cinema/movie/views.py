import io
from django.shortcuts import render, redirect

from .forms import movieScore_form
from .models import Movie
from .torrent import make_magnet_from_file
from django.core.files import File


def all_things(request):
   movies = Movie.objects.all()
   return render(request, 'ListOfFilms.html', {'movies': movies})

def all_films(request):
   movies = Movie.objects.filter(type = 2)
   return render(request, 'ListOfFilms.html', {'movies': movies})

def all_animes(request):
   movies = Movie.objects.filter(type = 1)
   return render(request, 'ListOfFilms.html', {'movies': movies})

def all_serials(request):
   movies = Movie.objects.filter(type = 3)
   return render(request, 'ListOfFilms.html', {'movies': movies})


def player(request, film_id):
   film = Movie.objects.get(movieId=film_id)
   magnet = make_magnet_from_file(film_id)
   return render(request, 'player.html', {'film': film, 'magnet': magnet})

global movie
def total_score(request, film_id):
   if request.method == "POST":
      print('okey')
      score = request.POST["estimation"]
      movie = Movie.objects.get(movieId=film_id)
      if movie.inter_score == None:
         movie.inter_score = float(score)
      else:
         movie.inter_score = movie.inter_score + float(score)
      if movie.NUsersEstimated == None:
         movie.NUsersEstimated = 1
      else:
         movie.NUsersEstimated += 1
      movie.movieTotalScore = movie.inter_score / movie.NUsersEstimated
      movie.save()
      print(movie.movieTotalScore)
   return redirect("http://127.0.0.1:8000/" + "movie/" + str(film_id))
