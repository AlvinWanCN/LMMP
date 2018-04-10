from django.shortcuts import render_to_response
from News.models import *



def base(request):
    return render_to_response('base.html',locals())

def new_list(request):
    news = News.objects.filter(dalete_flag='N').order_by('date')
    return render_to_response("new_list.html",locals())

def content(request,src):
    new = News.objects.get(src=src)
    return render_to_response("content.html",locals())
# Create your views here.


def reqTest(request):
    return render_to_response('reqTest.html',locals())