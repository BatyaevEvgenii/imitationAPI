from django.contrib import admin

# Register your models here.

from .models import Article, Author


admin.site.register(Author)
admin.site.register(Article)

