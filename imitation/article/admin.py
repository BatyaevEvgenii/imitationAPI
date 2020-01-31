from django.contrib import admin

# Register your models here.

from .models import Article, Author


# admin.site.register(Author)
# admin.site.register(Article)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(Author, AuthorAdmin)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author')



