from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        
    GENRE_CHOICES = (
        ('comedy', '코미디'),
        ('horror', '공포'),
        ('romance', '로맨스'),
    )

    genre = forms.ChoiceField(choices=GENRE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    score = forms.DecimalField(max_digits=2, decimal_places=1, widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.5', 'min': '0', 'max': '5'}))
    release_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))