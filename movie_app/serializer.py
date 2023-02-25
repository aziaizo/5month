from rest_framework import serializers
from .models import Review,Director,Movie
from django.db.models import Avg



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='id text stars'.split()

class DirectorSerializer(serializers.ModelSerializer):
    movie_count=serializers.SerializerMethodField
    class Meta:
        model=Director
        fields='id name movie_count'.split()

    @staticmethod
    def get_movie_count(director):
        return director.movie_count


class MovieSerializer(serializers.ModelSerializer):
    director=DirectorSerializer()
    movie_reviews=ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()
    class Meta:
        model=Movie
        fields='title description duration director director_name movie_reviews rating'.split()

    @staticmethod
    def get_rating(obj):
        return obj.movie_reviews.all().aggregate(Avg('stars'))

class ReviewSerializer(serializers.ModelSerializer):
    movie=MovieSerializer()
    class Meta:
        model=Review
        fields='__all__'