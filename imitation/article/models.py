from django.db import models

# Create your models here.

# модель авторов
class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    # удобочитаемое отображение объектов Author
    def __str__(self):
        return self.name

# модель статей
class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)

    # удобочитаемое отображение объектов Article
    def __str__(self):
        return self.title