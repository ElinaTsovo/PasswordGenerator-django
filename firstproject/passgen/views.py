import random
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.

def home(request): 
    return render(request, 'home.html')

def passgen(request):
    char = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('digits'):
        char.extend(list('0123456789'))
    if request.GET.get('symbol'):
        char.extend(list('+-*/@#$%^^'))

    length = int(request.GET.get('length', 10))
    
    password = ""

    for x in range(6):
        password += random.choice(char)
       
    return render(request, 'password.html', {'password':password})