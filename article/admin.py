from django.contrib import admin

from .models import Article,Comment

# Register your models here.

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_day"]

    list_display_links = ["title","created_day"]

    search_fields = ["title"]

    list_filter = ["created_day"]

    class Meta:
        model = Article
