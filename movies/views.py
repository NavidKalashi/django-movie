from django.shortcuts import render, redirect

from .models import Movie
from .forms import MovieForm

def movies(request):
    movies = Movie.objects.all()

    context = {'movies': movies}
    return render(request, 'movies/movies.html', context)

def addMovie(request):
    form = MovieForm()
    
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies')
        
    context = {'form': form}
    return render(request, 'movies/add-movie.html', context)

def editMovie(request, pk):
    movie = Movie.objects.get(id=pk)
    form = MovieForm(instance=movie)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies')

    context = {'form': form}
    return render(request, 'movies/add-movie.html', context)
    
def deleteMovie(request, pk):
    movie = Movie.objects.get(id=pk)
    
    if request.method == 'POST':
        movie.delete()
        return redirect('movies')

    context = {'movie': movie}
    return render(request, 'movies/delete-movie.html', context)