from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
# Create your views here.
def wishes(request):
    return HttpResponse("good morning")
def welcome(request):
    return HttpResponse("hello world")
def dateandtime(request):
    now=datetime.now()
    return HttpResponse("<h1>the current system date and time is: "\
        +str(now)+"</h1>")

