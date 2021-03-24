from django.db import models
from django.contrib.auth.models import User


# 文章分类
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='分类')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name


# 文章标签
class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name='标签')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    title = models.CharField(max_length=100, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    view = models.IntegerField(default=0, verbose_name='阅读量')
    is_top = models.BooleanField(default=False, verbose_name='置顶')
    slug = models.SlugField(unique=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_date = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tag = models.ManyToManyField(Tag, verbose_name='标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']

    def __str__(self):
        return self.title[:20]


# 友情链接
class FriendLink(models.Model):
    name = models.CharField(max_length=50, verbose_name='网站名称')
    description = models.CharField(max_length=100, verbose_name='网站描述')
    logo = models.URLField(blank=True, verbose_name='网站LOGO')
    link = models.URLField(verbose_name='网站地址')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_show = models.BooleanField(default=False, verbose_name='显示')
    is_active = models.BooleanField(default=True, verbose_name='有效')

    class Meta:
        verbose_name = '友链'
        verbose_name_plural = verbose_name
        ordering = ['-create_date']

    def __str__(self):
        return self.name
