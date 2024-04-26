from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Eat no meat fro entire month January")


def indexfeb(request):
    return HttpResponse("febraury  challenges are coming up")


def monthly_challenge(request, month):
    if month == 'january':
        message = "Eat no meat fro entire month January"
    elif month == 'february':
        message = "febraury  challenges are coming up"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(message)
