from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Player(models.Model):
  games = models.ManyToManyField('Game')
  player_name = models.OneToOneField('BoardState', on_delete = models.PROTECT)
  
  
class Game(models.Model):
  ruleset = models.ForeignKey('RuleSet', on_delete = models.PROTECT)
  board_state = models.OneToOneField('BoardState', on_delete = models.PROTECT)
  game_log = models.OneToOneField('GameLog', on_delete = models.PROTECT)
  owner = models.ForeignKey('Player', on_delete = models.PROTECT)
  

class BoardState(models.Model):
  piles = models.ManyToManyField('Pile')
  player_to_move = models.ForeignKey('Player', on_delete = models.PROTECT)
  pass

class GameLog(models.Model):
  moves = models.ManyToManyField('Move')
  pass

class RuleSet(models.Model):
  pass

class Move(models.Model):
  pass


class Card(models.Model):
  class Suit(models.IntegerChoices):
        DIAMOND = 1
        SPADE = 2
        HEART = 3
        CLUB = 4

  suit = models.IntegerField(choices=Suit.choices)
  
  value = models.CharField(max_length=250)
  isVisible = models.CharField(max_length=100)
  isbn = models.CharField(max_length=13)
  
  def __str__(self):
    return self.title

class Pile(models.Model):
  #cards = models.
  pass

class LegalMove(models.Model):
  pass

class Condition(models.Model):
  pass

class PlayerRank(models.Model):
  pass