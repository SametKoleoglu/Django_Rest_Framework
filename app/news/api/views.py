from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from news.models import *
from news.api.serializers import *


from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class JournalistListCreateAPIView(APIView):

    def get(self, request):
        journalists = Journalist.objects.all()
        serializer = JournalistSerializer(
            journalists, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsListCreateAPIView(APIView):

    def get(self, request):
        news = News.objects.filter(active=True)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsDetailAPIView(APIView):

    def get_object(self, pk):
        news = get_object_or_404(News, id=pk)
        return news

    def get(self, request, pk):
        news = self.get_object(pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    def put(self, request, pk):
        news = self.get_object(pk)
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        news = self.get_object(pk)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def news_list_create_api_view(request):
#     if request.method == 'GET':
#         news = News.objects.filter(active=True)
#         serializer = NewsSerializer(news, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = NewsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET',"PUT","DELETE"])
# def news_detail_api_view(request, pk):
#     try:
#         news = News.objects.get(id=pk)
#     except News.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = NewsSerializer(news)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = NewsSerializer(news, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         news.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
