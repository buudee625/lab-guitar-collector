from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Guitar, Review, Player
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
    not_players = Player.objects.exclude(id__in = guitar.players.all().values_list('id'))
    review_form = ReviewForm()
    return render(req, 'guitars/detail.html', {
        'guitar': guitar,
        'review_form': review_form,
        'players': not_players,
        })

def assoc_player(req, gtr_id, player_id):
    current_gtr = Guitar.objects.get(id=gtr_id)
    current_gtr.players.add(player_id)
    return redirect('detail', gtr_id=gtr_id)

def deassoc_player(req, gtr_id, player_id):
    current_gtr = Guitar.objects.get(id=gtr_id)
    current_ply = Player.objects.get(id=player_id)
    current_ply.guitar_set.remove(current_gtr)
    return redirect('detail', gtr_id=gtr_id)

class GtrCreate(CreateView):
    model = Guitar
    fields = ['brand', 'kind', 'model', 'string', 'released']

class GtrUpdate(UpdateView):
    model = Guitar
    fields = ['brand', 'kind', 'model', 'string', 'released']

class GtrDelete(DeleteView):
    model = Guitar
    success_url = '/guitars/'

def add_review(req, gtr_id):
    form = ReviewForm(req.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.guitar_id = gtr_id
        new_review.save()

    return redirect('detail', gtr_id=gtr_id)

class PlayerIndex(ListView):
    model = Player

class PlayerDetail(DetailView):
    model = Player

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['name', 'country', 'age']

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'