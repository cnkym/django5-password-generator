from django.shortcuts import render
from django.http import HttpResponse # v01.for return a http response message

# Create your views here.

def home(requests): # v01.add a function for Home page
    return HttpResponse("Hello World!")