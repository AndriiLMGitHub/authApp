from django.shortcuts import render
import random

# Create your views here.
def context_password():
    upper = 'ABCDEFGIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefgijklmnopqrstuvwxyz'
    symbols = '!@#$%^&*()_+?|<>:;{}`'
    numbers = '1234567890'

    password_length = 50

    all_types = upper + lower + symbols + numbers

    password = ''.join(random.sample(all_types, password_length))

    context = {'password' : password}

    return context


def home(request):
    return render(request, 'home/index.html', context_password())
