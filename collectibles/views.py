from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

# Create your views here.

# Players Views
class AboutView(View):
    """
    GET: information about the game.
    """
    template_name = 'form_template.html'

    def get(self, request):
        return HttpResponse(f'Bienvenidos a {settings.NAME}')

class StartView(View):
    """
    GET: initial point for any new player.

    POST: add a new player to the game.
    """

    template_name = ''
    def get(self, request):
        return HttpResponse(f'START')

    def post(self, request):
        return redirect('player')

class PlayerView(View):
    """
    GET: information about the player: id, leaderboard, stats and progress.

    """
    template_name = ''
    def get(self, request):
        return HttpResponse(f'Me')

class ScanView(View):
    """
    GET: a QR scanner, if you find redirect to item's view.

    POST: add a scanned item to player's collection.
    """
    template_name = ''
    def get(self, request):
        return HttpResponse(f"Scanner QR")

    def post(self, request):
        return redirect('item', itemId=0)

class MapView(View):
    """
    GET: render a UTFSM's map, display player's position.
    # TODO: Definir si usar un mapa de verdad usando la ubicación
    """
    template_name = ''
    def get(self, request, *args, **kwargs):
        return HttpResponse(f"Soy el mapa")

class CongratulationsView(View):
    """
    GET: You Won!
    """

    template_name = ''
    def get(self, request):
        return HttpResponse('<body><iframe width="560" height="315" src="https://www.youtube.com/embed/hf1DkBQRQj4" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></body>')


class ItemView(View):
    """
    GET: display item, information about the place and the collectible
    """
    template_name = ''
    def get(self, request, item_id):
        return HttpResponse(f"Soy el item {item_id}")


# Admin's Views
class DashboardView(View):
    """
    GET: display app stats
    """
    template_name = ''

    def get(self, request):
        return HttpResponse("Dashboard")


class ItemsView(View):
    """
    Get: display a GUI to print item's QR
    """

    def get(self, request):
        return HttpResponse("PRINT")
