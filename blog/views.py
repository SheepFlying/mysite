from django.shortcuts import render
from django.views import generic
from .models import Category, Tag, Article, FriendLink


class IndexView(generic.ListView):
    model = Article
    template_name = 'blog/index.html'




class Detail(generic.DetailView):
    pass
