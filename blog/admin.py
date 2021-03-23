from django.contrib import admin
from .models import Category, Tag, Article, FriendLink


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'views', 'create_date', 'update_date', 'is_top')
    list_display_links = ('title',)
    exclude = ('views',)
    list_editable = ('is_top',)


@admin.register(FriendLink)
class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'link', 'create_date', 'is_active', 'is_show')
    list_display_links = ('name',)
    list_editable = ('is_active', 'is_show')
