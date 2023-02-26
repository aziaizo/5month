from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import MovieSerializer,DirectorSerializer,\
    ReviewSerializer,MovieValidateSerializer,DirectorValidateSerializer,ReviewValidSerializer
from .models import Movie,Director,Review


@api_view(['GET','POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movie=Movie.objects.all()
        serializer=MovieSerializer(movie, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        title=request.data.get('title')
        description=request.data.get('description')
        duration=request.data.get('duration')
        director_id=request.data.get('director_id')
        movie=Movie.objects.create(title=title, description=description,
                                   duration=duration, director_id=director_id)

        return Response(data={'message':'Data received!',
                              'movie':MovieSerializer(movie).data},
                        status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT','DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie=Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'detail':'movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=MovieSerializer(movie)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data={'message':'Data received!',
                              'movie':MovieSerializer(movie).data})


@api_view(['GET','POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        director=Director.objects.all()
        serializer=DirectorSerializer(director, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        name=request.data.get('name')
        director=Director.objects.create(name=name)
        return Response(data={'message':'Data received!',
                              'director':DirectorSerializer(director).data},
                        status=status.HTTP_201_CREATED)

@api_view(['GET','DELETE','PUT'])
def director_detail_api_view(request, id):
    try:
        director=Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'detail':'director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=DirectorSerializer(director)
        return Response(data=serializer.data)
    if request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        director.name=request.data.get('name')
        director.save()
        return Response(data={'message':'Data received!',
                              'director':DirectorSerializer(director).data})
@api_view(['GET','POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        review=Review.objects.all()
        serializer=ReviewSerializer(review, many=True)
        return Response(data=serializer.data)
    if request.method == 'POST':
        serializer = ReviewValidSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        text=request.data.get('text')
        stars=request.data.get('stars')
        movie_id=request.data.get('movie_id')
        review=Review.objects.create(text=text, stars=stars, movie_id=movie_id)
        return Response(data={'message': 'Data received!',
                              'review': ReviewSerializer(review).data},
                        status=status.HTTP_201_CREATED)

@api_view(['GET','DELETE','PUT'])
def review_detail_api_view(request, id):
    try:
        review=Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'detail':'review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=ReviewSerializer(review)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviewValidSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data={'message': 'Data received!',
                              'review': ReviewSerializer(review).data})
