from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Card, Pile, Game, GameLog, PlayerRank
class CardListView(ListView):
  model = Card
  template_name = 'card_list.html'