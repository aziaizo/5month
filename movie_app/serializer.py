from rest_framework import serializers
from .models import Review,Director,Movie
from django.db.models import Avg
from rest_framework.exceptions import ValidationError


#
# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Review
#         fields='id text stars'.split()

class DirectorSerializer(serializers.ModelSerializer):
    movie_count=serializers.SerializerMethodField
    class Meta:
        model=Director
        fields='id name movie_count'.split()

    @staticmethod
    def get_movie_count(director):
        return director.movie_count


class MovieSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    class Meta:
        model=Movie
        fields='id title description duration  rating'.split()

    @staticmethod
    def get_rating(obj):
        return obj.movie_reviews.all().aggregate(Avg('stars'))


class ReviewSerializer(serializers.ModelSerializer):
    movie=MovieSerializer()
    class Meta:
        model=Review
        fields='__all__'



class MovieValidateSerializer(serializers.Serializer):
    title= serializers.CharField(max_length=100,min_length=1)
    description = serializers.CharField(max_length=200,min_length=2)
    duration = serializers.IntegerField()
    director_id = serializers.IntegerField()

    @staticmethod
    def validate_director_id(director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('This director does not exists!')
        return director_id



class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2)


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=2)
    stars = serializers.IntegerField(min_value=1,max_value=5)
    movie_id = serializers.IntegerField()


    @staticmethod
    def validate_movie_id(movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('This movie does not exists!')
