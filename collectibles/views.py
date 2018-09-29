from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings

from .forms import PlayerFrom
from .models import Player


# Auxiliary functions
def is_player(view_method):
    """Decorator, check if the request is from a player"""

    def new_view_method(self, request, **kwargs):
        player_id = request.session.get("player_id", None)
        if player_id is not None:
            return view_method(self, request, **kwargs)
        else:
            return redirect('about')

    return new_view_method


# Create your views here.

# Index view
class AboutView(View):
    """
        GET: information about the game.
        """
    template_name = 'about.html'

    @staticmethod
    def get_context_data():
        ctx = {'titulo': settings.NAME, "show_ctx": settings.DEBUG}
        return ctx

    def get(self, request):
        return render(
            request,
            AboutView.template_name,
            context=self.get_context_data()
        )


# Players Views
class StartView(View):
    """
    GET: initial point for any new player.

    POST: add a new player to the game.
    """

    template_name = 'player/start.html'

    @staticmethod
    def get_context_data():
        ctx = {
            'titulo': settings.NAME,
            'form': PlayerFrom(),
            "show_ctx": settings.DEBUG
        }
        return ctx

    def get(self, request):
        player_id = request.session.get("player_id", None)

        # Is already playing?
        if player_id is None:
            return render(
                request,
                StartView.template_name,
                context=StartView.get_context_data()
            )
        else:
            return redirect('player')

    def post(self, request):
        form = PlayerFrom(request.POST)
        if form.is_valid():
            # New DB instance
            nick = form.cleaned_data["nick"]
            new_player = Player.create(nick)
            new_player.save()

            # Save id player in session
            request.session["player_id"] = new_player.player_id

            return redirect('player')
        return redirect('about')


class PlayerView(View):
    """
    GET: information about the player: id, leaderboard, stats and progress.

    """
    template_name = 'player/player.html'

    @staticmethod
    def get_context_data(player):
        ctx = {
            'titulo': settings.NAME,
            'player_id': player.player_id,
            'player': player,
            # 'items': items,
            'show_ctx': settings.DEBUG}
        return ctx

    @is_player
    def get(self, request):
        player_id = request.session["player_id"]
        player = Player.objects.get(player_id=player_id)
        return render(
            request,
            PlayerView.template_name,
            context=PlayerView.get_context_data(player)
        )


class ScanView(View):
    """
    GET: a QR scanner, if you find redirect to item's view.

    POST: add a scanned item to player's collection.
    """
    template_name = 'player/scan.html'

    @staticmethod
    def get_context_data(player):
        ctx = {
            'titulo': settings.NAME,
            'player_id': player.player_id,
            'player': player,
            'show_ctx': settings.DEBUG}
        return ctx

    @is_player
    def get(self, request):
        player_id = request.session.get["player_id"]
        player = Player.objects.get(player_id=player_id)
        return render(
            request,
            ScanView.template_name,
            context=ScanView.get_context_data(player)
        )

    def post(self, request):
        return redirect('item', itemId=0)


class MapView(View):
    """
    GET: render a UTFSM's map, display player's position.
    # TODO: Definir si usar un mapa de verdad usando la ubicación
    """
    template_name = 'player/map.html'

    @staticmethod
    def get_context_data(player):
        ctx = {
            'titulo': settings.NAME,
            'player_id': player.player_id,
            'player': player,
            'show_ctx': settings.DEBUG}
        return ctx

    @is_player
    def get(self, request):
        player_id = request.session.get("player_id", None)
        player = Player.objects.get(player_id=player_id)
        return render(
            request,
            MapView.template_name,
            context=MapView.get_context_data(player)
        )


class CongratulationsView(View):
    """
    GET: You Won!
    """

    template_name = 'player/congratulations.html'

    def get_context_data(self):
        ctx = {'titulo': settings.NAME, "show_ctx": settings.DEBUG}
        return ctx

    @is_player
    def get(self, request):
        return render(
            request,
            CongratulationsView.template_name,
            context=self.get_context_data()
        )


class ItemView(View):
    """
    GET: display item, information about the place and the collectible
    """
    template_name = 'player/item.html'

    def get_context_data(self):
        ctx = {'titulo': settings.NAME, "show_ctx": settings.DEBUG}
        return ctx

    @is_player
    def get(self, request, item_id):
        return render(
            request,
            ItemView.template_name,
            context=self.get_context_data()
        )
