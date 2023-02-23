from rest_framework import serializers
from .models import Review,Director,Movie

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Director
        fields='__all__'


class MovieSerializer(serializers.ModelSerializer):
    director=DirectorSerializer()
    class Meta:
        model=Movie
        fields='title description duration director'.split()



class ReviewSerializer(serializers.ModelSerializer):
    movie=MovieSerializer()
    class Meta:
        model=Review
        fields='__all__'