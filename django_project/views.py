from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def base(request):
    return HttpResponse(request, "Success")

def home(request):
    return HttpResponse(request, "Success")
def index(request):
    return HttpResponse(request, "Success")

def login(request):
    return HttpResponse(request, "Success")
