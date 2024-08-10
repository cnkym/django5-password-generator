from django.shortcuts import render
import random

# Create your views here.

def home(requests): # v01.add a function for Home page
    return render(requests, # v01.use tamplate
                  'generator/home.html',    # template html file
                  {'msg' : "Hello World!"}, # dict format message
                  )

def password(requests): # v03.add a form forpassword page

    def contains_special(s, special_characters = "!#$%&@"):
        '''
        checking a string contains special character or not.   
        Args:   
            s (str): string to be checked
            special_characters(str): special character
        Retruns:   
            bool: True means ontains, False means none   
        '''
        return any(c in special_characters for c in s)

    characters = list('abcdefghijkmnopqrstuvwxyz')
    if requests.GET.get('numbers'):
        characters.extend(list("234567892345678923456789"))
    if requests.GET.get('special'):
        characters.extend(list("!#$%&@!#$%&@!#$%&@!#$%&@"))
    if requests.GET.get('uppercase'):
        characters.extend(list("ABCDEFGHJKLMNPQRSTUVWXYZ"))

    length = int(requests.GET.get('length',8))

    retry = [False, False, False, False] # lowercase, uppercase, numbers, special
    test = [0, 0, 0, 0]
    while not all(retry):
        thepassword = ''
        for x in range(length):
            thepassword += random.choice(characters)

        if any(map(str.islower, thepassword)):
            retry[0] = True
            test[0] = 1
        else:
            retry[0] = False
            test[0] = 0

        if requests.GET.get('uppercase'):
            if any(map(str.isupper, thepassword)):
                retry[1] = True
                test[1] = 1
            else:
                retry[1] = False
                test[1] = 0
        else:
            retry[1] = True
            test[1] = 2

        if requests.GET.get('numbers'):
            if any(map(str.isdecimal, thepassword)):
                retry[2] = True
                test[2] = 1
            else:
                retry[2] = False
                test[2] = 0
        else:
            retry[2] = True
            test[2] = 2

        if requests.GET.get('special'):
            if any(map(contains_special, thepassword)):
                retry[3] = True
                test[3] = 1
            else:
                retry[3] = False
                test[3] = 0
        else:
            retry[3] = True
            test[3] = 2
        #print(test)

    return render(requests,
                  'generator/password.html',    # passwoed html page
                  {'password' : thepassword},   # dict format message
                  )