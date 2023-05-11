from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from .models import Actor, Movie, Review
from .serializers import ActorSerializer, MovieSerializer, ReviewSerializer, ActorDetailSerializer, MovieDetailSerializer, ReviewDetailSerializer, ReviewCreateSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def actor_list(request):
    actors = get_list_or_404(Actor)
    serializer = ActorSerializer(actors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def actor_detail(request, actor_id):
    actor = get_object_or_404(Actor, id=actor_id)
    serializer = ActorDetailSerializer(actor)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def review_list(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ReviewDetailSerializer(review, request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        review.delete()
        msg = {"delete":f'{review_id}번 리뷰 삭제'}
        return Response(msg, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = ReviewCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)