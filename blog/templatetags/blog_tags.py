from django.template import Library
from django.db.models import Count
from ..models import Category, Tag, Article, FriendLink

register = Library()


@register.simple_tag
def get_tag_list():
    return Tag.objects.annotate(article_num=Count('article')).filter(article_num__gt=0)


@register.simple_tag
def get_category_list():
    return Category.objects.annotate(article_num=Count('article')).filter(article_num__gt=0)


@register.simple_tag
def get_friend_link_list():
    return FriendLink.objects.filter(is_show=True, is_active=True)

