

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils import timezone


class UserInfo(AbstractUser):
    id = models.CharField(primary_key=True,unique=True,max_length=20)
    status = models.CharField('状态1未审核2审核中3审核通过',max_length=1,default=1)
    phone = models.CharField(max_length=11)

    createTime = models.DateTimeField('创建日期',default=timezone.now)
    updateTime = models.DateTimeField('修改日期',auto_now=True)
    end_vip_time = models.DateTimeField('vip到期日',auto_now=True)
    business_flag = models.CharField('1营业中，2暂停营业',max_length=1)
    image_url = models.CharField(max_length=100)
    image_url_id = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    tag = models.CharField(max_length=10)
class MerchantInfo(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=20)
    status = models.CharField('状态1未审核2审核中3审核通过', max_length=1, default=1)
    phone = models.CharField(max_length=11)
    name  = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    createTime = models.DateTimeField('创建日期', default=timezone.now)
    updateTime = models.DateTimeField('修改日期', auto_now=True)
    end_vip_time = models.DateTimeField('vip到期日',auto_now=True)
    business_flag = models.CharField('1营业中，2暂停营业', max_length=1)
    image_url = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    tag = models.CharField(max_length=10)
class Food(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=20)
    merchant_id = models.CharField(max_length=20)
    image_url = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    type = models.CharField(max_length=1)
    status = models.CharField('上架，2下架',max_length=1)
    createTime = models.DateTimeField('创建日期', default=timezone.now)
    updateTime = models.DateTimeField('修改日期', auto_now=True)

class Images(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=20)
    merchant_id = models.CharField(max_length=20)
    image_url = models.CharField(max_length=100)
    food_id = models.CharField(max_length=20)
    user_id = models.CharField(max_length=20)
    createTime = models.DateTimeField('创建日期',default=timezone.now)
    updateTime = models.DateTimeField('修改日期', auto_now=True)
