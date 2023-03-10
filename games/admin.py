from django.contrib import admin

# Register your models here.
from .models import Card, Pile, PlayerRank, GameLog, Game
admin.site.register(Card)
admin.site.register(Pile)
admin.site.register(PlayerRank)
admin.site.register(GameLog)
admin.site.register(Game)