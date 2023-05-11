from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content')


class ActorMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)


class ActorDetailSerializer(serializers.ModelSerializer):
    movies = ActorMovieSerializer(read_only=True, many=True)
    class Meta:
        model = Actor
        fields = '__all__'

class MovieActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name',)

class MovieDetailSerializer(serializers.ModelSerializer):

    review_count = serializers.IntegerField(source='review_set.count', read_only=True)
    actors = MovieActorSerializer(read_only=True, many=True)
    review_set = ReviewSerializer(read_only=True, many=True)
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = ActorMovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'


class ReviewCreateSerializer(serializers.ModelSerializer):
    movie = ActorMovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields=('movie',)