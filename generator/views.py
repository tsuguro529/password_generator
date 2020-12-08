from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'hui43orhwo'})

def eggs(request):
    return HttpResponse('<h1>卵美味しい</h1>')
