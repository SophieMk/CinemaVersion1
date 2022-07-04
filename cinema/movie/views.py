import io
from django.shortcuts import render
from .models import Movie
from .torrent import make_magnet_from_file
from django.core.files import File

# Create your views here.


def all_films(request):
   movies = Movie.objects.all()
   return render(request, 'ListOfFilms.html', {'movies': movies})


def player(request, film_id):
   film = Movie.objects.get(movieId=film_id)
   magnet = make_magnet_from_file(film_id)
   print("Default buffer size:", io.DEFAULT_BUFFER_SIZE)
   file = open(film.torrent.path, mode="r", buffering=5)
   print(file.line_buffering)
   file_contents = file.buffer
   return render(request, 'player.html', {'film': film, 'magnet': magnet, 'torrentBuf': file_contents})

