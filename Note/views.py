import json

from django.contrib import auth
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import logging
from Note import models
from Note.forms import VmaigUserCreationForm

logger = logging.getLogger(__name__)
#个人注册

def  registPersonal(request):

    username = request.POST.get("username", "")
    password = request.POST.get("password", "")

    form = VmaigUserCreationForm(request.POST)
    errors = []

    if request.method == 'POST':
      if form.is_valid():
         form.save()
         return res(request, "true")
      else:
          for k, v in form.errors.items():
              # v.as_text() 详见django.forms.util.ErrorList 中
              errors.append(v.as_text())
      mydict = {"errors": errors}
      return res(request,"false",mydict)
    return render(request, 'personal_user/regist.html', {'obj': form})



def  loginPersonal(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    user = auth.authenticate(username=username, password=password)

    errors = []

    if user is not None:
        auth.login(request, user)
    else:
        errors.append(u"密码或者用户名不正确")

    mydict = {"errors": errors}
    return HttpResponse(
        json.dumps(mydict),
        content_type="application/json"
    )

def logout(self, request):
    if not request.user.is_authenticated():
        logger.error(u'[UserControl]用户未登陆')
        raise PermissionDenied
    else:
        auth.logout(request)
        return HttpResponse('OK')

def  updatePersonal(request):
    models.UserInfo.username

def  list(request):
    models.UserInfo.username


def res(request,success,data,code,msg):
    result = {"success":success,"data":data,"errorCode":code,"msg":msg}
    #json返回为中文
    return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")