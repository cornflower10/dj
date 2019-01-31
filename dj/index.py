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



