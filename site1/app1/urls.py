from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/',views.index),
    path('/1',views.index1) #Duong dan of trang web la app1/1
]
