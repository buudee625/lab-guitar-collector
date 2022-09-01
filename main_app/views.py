from django.shortcuts import render
from .models import Guitar, Review
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
from django.http import HttpResponse

def home(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

def guitar_index(req):
    guitars = Guitar.objects.all()
    return render(req, 'guitars/index.html', {'guitars': guitars})

def guitar_detail(req, gtr_id):
    guitar = Guitar.objects.get(id=gtr_id)
    return render(req, 'guitars/detail.html', {'guitar': guitar})

class GtrCreate(CreateView):
    model = Guitar
    fields = '__all__'

class GtrUpdate(UpdateView):
    model = Guitar
    fields = ['brand', 'kind', 'model', 'released']

class GtrDelete(DeleteView):
    model = Guitar
    success_url = '/guitars/'