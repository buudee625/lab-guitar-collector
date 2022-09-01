from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Guitar, Review
from .forms import ReviewForm
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
    review_form = ReviewForm()
    return render(req, 'guitars/detail.html', {'guitar': guitar, 'review_form': review_form})

def add_review(req, gtr_id):
    form = ReviewForm(req.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.gtr_id = gtr_id
        new_review.save()
    
    return redirect('detail', gtr_id=gtr_id)

class GtrCreate(CreateView):
    model = Guitar
    fields = '__all__'

class GtrUpdate(UpdateView):
    model = Guitar
    fields = ['brand', 'kind', 'model', 'released']

class GtrDelete(DeleteView):
    model = Guitar
    success_url = '/guitars/'