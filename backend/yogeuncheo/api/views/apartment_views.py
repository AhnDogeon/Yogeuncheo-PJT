from rest_framework import status
from rest_framework.decorators import api_view
from api.models import *
from api.serializers import *
from rest_framework.response import Response
import random
from django.http import JsonResponse

@api_view(['GET', 'POST', 'DELETE'])
def movies(request):
    # if request.method == 'GET':
    #     id = request.GET.get('id', request.GET.get('apartment_id', None))
    #     movies = Movie.objects.all()
    #     movies = movies.filter(pk=id)
    #     serializer = MovieSerializer(movies, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)
    #
    # if request.method == 'DELETE':
    #     movie = Movie.objects.all()
    #     movie.delete()
    #     return Response(status=status.HTTP_200_OK)
    #
    # if request.method == 'POST':
    #     movies = request.data.get('movies', None)
    #     for movie in movies:
    #         id = movie.get('id', None)
    #         title = movie.get('title', None)
    #         genres = movie.get('genres', None)
    #         Movie(id=id, title=title, genres='|'.join(genres)).save()
    return Response(status=status.HTTP_200_OK)