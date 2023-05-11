from django.shortcuts import render, redirect
from .forms import MovieForm, CommentForm
from .models import Movie, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid:
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'movies/detail.html', context)

@login_required
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', pk=movie.pk)
        else:
            form = MovieForm(instance=movie)
    else:
        return redirect('movies:detail', movie.pk)
    context = {
        'form': form,
        'movie': movie
    }
    return render(request, 'movies/update.html', context)

@require_http_methods(['POST'])
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user == movie.user:
        movie.delete()
        return redirect('movies:index')
    return redirect('movies:detail', movie.pk)


@login_required
def comments_create(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()
    return redirect('movies:detail', movie.pk)


def comments_delete(request, pk, comment_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('movies:detail', pk)

@login_required
def likes(request, movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
        return redirect('movies:index')
    return redirect('accounts:login')