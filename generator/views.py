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

    def check_result(requests, type, function, result, index):
        if requests.GET.get(type):
            if any(map(function, result)):
                retry[index] = True
                test[index] = 1
            else:
                retry[index] = False
                test[index] = 0
        else:
            retry[index] = True
            test[index] = 2
        #print(test)

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

        check_result( requests,
                        type='uppercase',
                        function=str.isupper,
                        result=thepassword,
                        index=1)

        check_result( requests,
                        type='numbers',
                        function=str.isdecimal,
                        result=thepassword,
                        index=2)

        check_result( requests,
                        type='special',
                        function=contains_special,
                        result=thepassword,
                        index=3)
        #print(test)

    return render(requests,
                  'generator/password.html',    # passwoed html page
                  {'password' : thepassword},   # dict format message
                  )

def about(requests):
    return render(requests,
                  'generator/about.html',
                  {'msg' : "This is about page!"},
                  )