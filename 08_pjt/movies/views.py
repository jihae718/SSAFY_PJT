from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_safe
from .models import Movie, Genre



# Create your views here.
@require_safe
def index(request):
    movies = get_list_or_404(Movie)
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {'movie':movie}
    return render(request, 'movies/detail.html', context )


@require_safe
def recommended(request):
    popular_movie = Movie.objects.order_by('-vote_average')[:10]
    context = { 'movies': popular_movie}
    return render(request, 'movies/recommended.html', context)