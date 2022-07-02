from django.shortcuts import render
from .models import Movie

# Create your views here.
def allFilms(request):
   movies = Movie.objects.all()
   return render(request,'ListOfFilms.html',{'movies':movies})