from .models import Movie, Comment
from django import forms

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = (
            'user',
            'like_users',
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = (
            'movie',
            'user',
        )
