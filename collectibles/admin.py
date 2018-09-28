from django.contrib import admin
from .models import Content, Item, Player, Location, AcquiredItem

# Register your models here.
admin.site.register(Content)
admin.site.register(Item)
admin.site.register(Player)
admin.site.register(Location)
admin.site.register(AcquiredItem)
