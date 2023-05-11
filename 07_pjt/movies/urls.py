from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.actor_list),
    path('actors/<int:actor_id>/', views.actor_detail),
    path('movies/', views.movie_list),
    path('movies/<int:movie_id>/', views.movie_detail),
    path('reviews/', views.review_list),
    path('reviews/<int:review_id>/', views.review_detail),
    path('movies/<int:movie_id>/reviews/', views.create_review)
]
