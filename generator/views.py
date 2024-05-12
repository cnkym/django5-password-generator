from django.shortcuts import render


# Create your views here.

def home(requests): # v01.add a function for Home page
    return render(requests, # v01.use tamplate
                  'generator/home.html',    # template html file
                  {'msg' : "Hello World!"}, # dict format message
                  )