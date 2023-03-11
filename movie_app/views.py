from .serializer import *
from .models import Movie,Director,Review
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination



class DirectorModelViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination


class MovieModelViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination


class ReviewModelViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewValidateSerializer

class ReviewDetailModelsViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewValidateSerializer


