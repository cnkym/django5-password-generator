from django.shortcuts import render
import random

# Create your views here.

def home(requests): # v01.add a function for Home page
    return render(requests, # v01.use tamplate
                  'generator/home.html',    # template html file
                  {'msg' : "Hello World!"}, # dict format message
                  )

def password(requests): # v03.add a form forpassword page

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if requests.GET.get('numbers'):
        characters.extend(list("123456789"))
    if requests.GET.get('special'):
        characters.extend(list("!#$%&"))
    if requests.GET.get('uppercase'):
        characters.extend(list("ABCDEFGHIJKLMNPQRSTUVWXYZ"))

    length = int(requests.GET.get('length',8))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(requests,
                  'generator/password.html',    # passwoed html page
                  {'password' : thepassword},   # dict format message
                  )