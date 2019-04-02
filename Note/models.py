

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils import timezone


class UserInfo(AbstractUser):
    id = models.AutoField(primary_key=True,unique=True,auto_created=True)
    status = models.CharField('状态1未审核2审核中3审核通过',max_length=1,default=1)
    phone = models.CharField(max_length=11,null=True, blank=True)
    createTime = models.DateTimeField('创建日期',default=timezone.now)
    updateTime = models.DateTimeField('修改日期',auto_now=True)
    end_vip_time = models.DateTimeField('vip到期日',null=True,blank=True)
    business_flag = models.CharField('1营业中，2暂停营业',max_length=1)
    image_url = models.ImageField(upload_to='img/user/%y%m%d',null=True,blank=True)
    desc = models.CharField(max_length=100,null=True, blank=True)
    location = models.CharField(max_length=50,null=True, blank=True)
    tag = models.CharField(max_length=10,null=True, blank=True)

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        for attr in fields:
            d[attr] = getattr(self, attr)

        import json
        return json.dumps(d)

class MerchantInfo(models.Model):
    id = models.AutoField(primary_key=True, unique=True,auto_created=True)
    status = models.CharField('状态1未审核2审核中3审核通过', max_length=1, default=1)
    phone = models.CharField(max_length=11,null=True, blank=True)
    name  = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    createTime = models.DateTimeField('创建日期', default=timezone.now)
    updateTime = models.DateTimeField('修改日期', auto_now=True)
    end_vip_time = models.DateTimeField('vip到期日',null=True, blank=True)
    business_flag = models.CharField('1营业中，2暂停营业', max_length=1)
    image_url = models.ImageField(upload_to='img/merchant/%y%m%d', null=True, blank=True)
    desc = models.CharField(max_length=100,null=True, blank=True)
    location = models.CharField(max_length=50,null=True, blank=True)
    tag = models.CharField(max_length=10,null=True, blank=True)
class Food(models.Model):
    merchant = models.ForeignKey(MerchantInfo,on_delete=models.CASCADE,verbose_name="商户")
    id = models.AutoField(primary_key=True, unique=True,auto_created=True)
    # merchant_id = models.BigIntegerField()
    image_url = models.ImageField(upload_to='img/food/%y%m%d',null=True,blank=True)
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    type = models.CharField(max_length=1)
    status = models.CharField('上架，2下架',max_length=1)
    createTime = models.DateTimeField('创建日期', default=timezone.now)
    updateTime = models.DateTimeField('修改日期', auto_now=True)

class Images(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name="食物" ,null=True,blank=True)
    merchant = models.ForeignKey(MerchantInfo, on_delete=models.CASCADE, verbose_name="商户",null=True,blank=True)
    userinfo = models.ForeignKey(UserInfo,on_delete=models.CASCADE,verbose_name="用户",null=True,blank=True)
    id = models.AutoField(primary_key=True, unique=True,auto_created=True)
    # merchant_id = models.BigIntegerField()
    image_url = models.ImageField(upload_to='img/common/%y%m%d')
    # food_id = models.BigIntegerField()
    # user_id = models.BigIntegerField()
    createTime = models.DateTimeField('创建日期',default=timezone.now)
    updateTime = models.DateTimeField('修改日期', auto_now=True)
