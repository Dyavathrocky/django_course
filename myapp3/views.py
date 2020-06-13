from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def morning(request):
    return HttpResponse("hi good morning")
def afternoon(request):
    return HttpResponse("hi how are you good afternoon")
def evening(request):
    return HttpResponse("hi good evenng")
def night(request):
    return HttpResponse("good night")
