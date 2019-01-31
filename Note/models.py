

from django.db import models

# Create your models here.
class User(models.Model):
    userInfoId = models.TextField()
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    imageUrl = models.TextField(null = True)
    ip = models.TextField(null = True)
    province = models.TextField(null = True)
    city = models.TextField(null = True)
    createTime = models.DateTimeField('创建日期',auto_now_add=True)
    updateTime = models.DateTimeField('修改日期',auto_now=True)

class UUser(models.Model):
    imageUrl = models.TextField(null = True)
    userInfoId = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    amount = models.FloatField(null = True)
    remark = models.CharField(max_length=100)
    relationship = models.TextField(null = True)
    createTime = models.DateTimeField('创建日期',auto_now_add=True)
    updateTime = models.DateTimeField('修改日期',auto_now=True)
