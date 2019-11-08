from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers




@api_view(['GET', 'POST', 'DELETE'])
def read_score(request):
    if request.method == 'GET':
        dong_name = request.GET.get('searchAddress', None)
        gu_name = request.GET.get('gu', None)
        dong2 = request.GET.get('dong2', None)
        print(dong2)

        if dong_name:
            address = TotalAddress.objects.get(address=dong_name)
            # 파이썬과 vue 언어를 변환시켜주는 거
            serializer = AddressSerializer(address)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        elif dong2:
            address = TotalAddress.objects.get(address=dong2)
            # 파이썬과 vue 언어를 변환시켜주는 거
            serializer = AddressSerializer(address)
            return Response(data=serializer.data, status=status.HTTP_200_OK)


        elif gu_name:

            dong_list = TotalAddress.objects.filter(gu__icontains=gu_name)

            temp_list = []
            for i in range(len(dong_list)):
                print(dong_list[i].dong)
                temp_list.append(dong_list[i].dong)
            # print(temp_list)
            # res = serializers.serialize('json', temp_list, ensure_ascii=False)
            return Response(data=temp_list, status=status.HTTP_200_OK)






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
