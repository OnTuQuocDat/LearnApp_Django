from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('On Tu Quoc Dat APP 1')

def index1(request):
    return HttpResponse('This is a child of app 1')