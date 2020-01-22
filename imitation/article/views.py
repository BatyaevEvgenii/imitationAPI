from django.shortcuts import render
from rest_framework.response import Response

# попробуем через APIView
from rest_framework.views import APIView

from .models import Article
from .serializer import ArticleSerializer

# Create your views here.


class ArticleView(APIView):
    # просмотр того что есть в статьях
    def get(self, request):
        articles = Article.objects.all()
        # преобразуем данные
        serializer = ArticleSerializer(articles, many=True)
        # return Response({"articles": articles})
        return Response({"articles": serializer.data})
