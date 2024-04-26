from . import views
from django.urls import path

urlpatterns =[
    path("january", views.index),
]