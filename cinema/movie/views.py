import io
from django.shortcuts import render

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


def total_score(request, film_id):
   if request.method == "POST":
      print('okey')
      score = request.GET.get('estimate', '')
      #score = form.cleaned_data.get("score")
      movie = Movie.objects.get(movieId=film_id)
      movie.nScore.inter_score += score
      movie.nScore.amount += 1
      movie.movieTotalScore = movie.nScore.inter_score / movie.nScore.amount
      print(movie.movieTotalScore)
         #HttpResponseRedirect()
   else:
      form = movieScore_form()
   return render(request, 'player.html', {'form': form})
