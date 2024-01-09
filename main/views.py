from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'home',

    }
    return render(request, 'main/index.html', context)