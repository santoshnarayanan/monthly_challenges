from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Eat no meat fro entire month January")

def indexfeb(request):
    return HttpResponse("febraury  challenges are coming up")