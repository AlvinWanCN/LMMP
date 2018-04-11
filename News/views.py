#coding:utf-8
from django.shortcuts import render_to_response
from News.models import *
from News.forms import *
import hashlib
from django.http import JsonResponse

def base(request):
    return render_to_response('base.html',locals())

def new_list(request):
    news = News.objects.filter(delete_flag='N').order_by('date')
    return render_to_response("new_list.html",locals())

def content(request,src):
    new = News.objects.get(src=src)
    return render_to_response("content.html",locals())
# Create your views here.


def reqTest(request):
    req_list = dir(request)
   # getData = request.GET['a']
    return render_to_response('reqTest.html',locals())

def forms(request):
    if request.method == "POST" and request.POST: #如果你提交的方式是post，并且有数据
        username = request.POST['username']  #username为我们前端html里面的name的值
        password=request.POST['password']
        hash = hashlib.md5()
        hash.update(password)
        password = hash.hexdigest()
        u = User()
        u.user = username
        u.password = password
        u.save()

    return render_to_response('forms.html',locals())


def djangoForms(request):
    if request.method == 'POST' and request.POST:
        register = Register(request.POST)
        if register.is_valid(): #判断是否校验是否成功
            data = register.cleaned_data #将校验成功的数据以字典的形式返回
    else:
        register = Register()
    return render_to_response("djangoForms.html",locals())

def djAlax(request):
    return render_to_response("django_ajax.html",locals())

def postData(request):
    if request.method == "POST" and request.POST:
        response_data = {'state':"you are success"}
    else:
        response_data = {"state":"you are done"}
    return JsonResponse(response_data)