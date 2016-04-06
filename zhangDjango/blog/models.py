from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)

# 一个类对应一个表
class Article(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.URLField()
    protal = models.ImageField()

    # 外扩展
    author = models.ForeignKey(Author)  # 这个Author 最好放在上面要不可能会找不到







