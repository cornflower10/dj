from django.core import serializers
from django.http import HttpResponse
import json
from Note import models
from django.http import JsonResponse

class Hello :
    def hello(self):
        print('hello')
h = Hello
def hello(request):
    # data = {'name':'dj','age':'18'}
    data = {}
    models.User.objects.create(userInfoId = '450238750498',name = 'djh',age = 18)
    users = models.User.objects.values()
    data['list'] = list(users)
    return JsonResponse(data)


def login(request):
    if request.method == 'POST':
        userInfoId = models.TextField()
        name = request.POST.get('name',None)
        age = models.IntegerField()
        imageUrl = models.TextField(null=True)
        ip = models.TextField(null=True)
        province = models.TextField(null=True)
        city = models.TextField(null=True)
        createTime = models.DateTimeField('创建日期', auto_now_add=True)
        updateTime = models.DateTimeField('修改日期', auto_now=True)



