from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# пробуем через APIView
from rest_framework.views import APIView

from .models import Article
from .serializer import ArticleSerializer

# Create your views here.

class ArticleView(APIView):
    # смотрим что есть в статьях
    def get(self, request, pk=None):
        # если запрашиваем по id
        if pk:
            article = get_object_or_404(Article.objects.all(), pk=pk)
            serializer = ArticleSerializer(article)
            return Response({"article": serializer.data})
        articles = Article.objects.all()
        # преобразуем все данные(many)
        serializer = ArticleSerializer(articles, many=True)
        # return Response({"articles": articles})
        return Response({"articles": serializer.data})

    def post(self, request):
        article = request.data.get('article')
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfuly".format(article_saved.title)})

    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        # partial = True для обновления некоторых полей
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' update successfully".format(article_saved.title)})

    def delete(self, request, pk):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "Article with id '{}' has been deleted.".format(pk)}, status=204)


