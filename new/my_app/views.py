from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import Topic, Webpage, AccessRecord
# Create your views here.

def help(request):
    web_list = Webpage.objects.order_by('topic')
    dict = {'insert': web_list}
    return render(request,'my_app/index.html',context=dict)

def index(request):
    return HttpResponse("welcome to my home page-amol karpe")

def help1(request):
    return HttpResponse("welcome to my help page-go to /amol")
