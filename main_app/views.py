from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

def guitar_index(req):
    return render(req, 'guitars/index.html', {'guitars': guitars})