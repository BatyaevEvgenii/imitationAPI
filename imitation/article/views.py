from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

# пробуем через APIView
from rest_framework.views import APIView

from .models import Article
from .serializer import ArticleSerializer

# Create your views here.

class ArticleList(APIView):
    # смотрим что есть в статьях
    def get(self, request, format=None):
        articles = Article.objects.all()
        # преобразуем все данные(many)
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request, format=None):
        article = request.data.get('article')
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
            return Response({"success": "Article '{}' created successfuly".format(article_saved.title)})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetail(APIView):

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response({"article": serializer.data})

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        data = request.data.get('article')
        # partial = True для обновления некоторых полей
        serializer = ArticleSerializer(article, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
            return Response({"success": "Article '{}' update successfully".format(article_saved.title)})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response({"message": "Article with id '{}' has been deleted.".format(pk)}, status=HTTP_204_NO_CONTENT)


