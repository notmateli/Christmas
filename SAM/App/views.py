from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("Hello MIT Class")

def emobilis(request):
    return HttpResponse(" This is Emobilis")

def home(request):
    return render(request, "home.html")


