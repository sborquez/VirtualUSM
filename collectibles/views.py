from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings

from .forms import PlayerFrom
from .models import Player, Location, Item


# Auxiliary decorators
def basic_context_data(prepare_context_data):
    """
        Add basic data to all Views.prepare_context_data()
    """
    basic_ctx = {
        'str_app': settings.CLIENT.app,
        'str_item': settings.CLIENT.item,
        'str_items': settings.CLIENT.items,
        'int_total_locations': settings.CLIENT.locations,

        'bool_show_ctx': settings.DEBUG,
    }

    def _new_view_method(*args, **kwargs):
        ctx = prepare_context_data(*args, **kwargs)
        return {**ctx, **basic_ctx}
    return _new_view_method


def is_player(view_request_handler):
    """
        Check if the request is from a player.

        Add the functionality of checking the client session variables. If the request is not from a player, it
        redirected to AboutView.
    """

    def _new_view_method(request, *args, **kwargs):
        player_id = request.session.get("player_id", None)
        # Player exist and is playing
        if player_id is not None:
            if Player.objects.filter(player_id=player_id, active=True).exists():
                return view_request_handler(request, *args, **kwargs)
            else:
                del request.session["player_id"]
                respond = redirect('about')
                # TODO mostrar mensaje de error
                respond = add_get_variables(respond, error="deactivate_player")
                return respond
        else:
            respond = redirect('about')
            # TODO mostrar mensaje de error
            respond = add_get_variables(respond, error="no_player")
            return respond
    return _new_view_method


# auxiliaries functions
def add_get_variables(respond, **kwargs):
    """
    Add the pair key:value form kwargs to a GET respond.

    This add variables to the url.
    """
    variables = "&".join([f"{key}={value}" for key, value in kwargs.items()])
    respond["Location"] += f"?{variables}"
    return respond


# Create your views here.

# Index view
class AboutView(View):
    """
        GET: information about the game.
    """

    template_name = 'about.html'

    @staticmethod
    @basic_context_data
    def prepare_context_data(player_id):
        ctx = {
            "player_id": player_id,
        }
        return ctx

    @staticmethod
    def get(request):
        player_id = request.session.get("player_id", 0)
        return render(
            request,
            AboutView.template_name,
            context=AboutView.prepare_context_data(player_id)
        )


# Players Views
class StartView(View):
    """
    GET: initial point for any new player.

    POST: add a new player to the game.
    """

    template_name = 'player/start.html'

    @staticmethod
    @basic_context_data
    def prepare_context_data():
        ctx = {
            'form': PlayerFrom(),
        }
        return ctx

    @staticmethod
    def get(request):
        player_id = request.session.get("player_id", None)

        # Is already playing?
        if player_id is None:
            return render(
                request,
                StartView.template_name,
                context=StartView.prepare_context_data()
            )
        else:
            return redirect('player')

    @staticmethod
    def post(request):
        form = PlayerFrom(request.POST)
        if form.is_valid():
            # New DB instance
            nick = form.cleaned_data["nick"]
            new_player = Player.create(nick)
            new_player.save()

            # Save id player in session
            request.session["player_id"] = new_player.player_id

            return redirect('player')
        respond = redirect('about')
        respond = add_get_variables(respond, error="invalid")
        return respond


class PlayerView(View):
    """
    GET: information about the player: id, leaderboard, stats and progress.

    """
    template_name = 'player/player.html'

    @staticmethod
    @basic_context_data
    def prepare_context_data(player):
        ctx = {
            'player_id': player.player_id,
            'player': player,          #'items': items,
        }
        return ctx

    @staticmethod
    @is_player
    def get(request):

        # TODO listar items
        # TODO Mostrar avance o posicion en la tabla

        player_id = request.session["player_id"]
        player = Player.objects.get(player_id=player_id)
        return render(
            request,
            PlayerView.template_name,
            context=PlayerView.prepare_context_data(player)
        )

    @staticmethod
    @is_player
    def post(request):
        """ Delete active player"""
        player_id = request.session["player_id"]
        player = Player.objects.get(player_id=player_id)
        player.deactivate()

        del request.session["player_id"]

        respond = redirect("about")
        # TODO mostrar mensaje de logout
        respond = add_get_variables(respond, logout="success")
        return respond


class ScanView(View):
    """
    GET: a QR scanner, if you find redirect to item's view.

    POST: add a scanned item to player's collection.
    """
    template_name = 'player/scan.html'

    @staticmethod
    @basic_context_data
    def prepare_context_data(player):
        ctx = {
            'player_id': player.player_id,
            'player': player,
        }
        return ctx

    @staticmethod
    @is_player
    def get(request):
        player_id = request.session["player_id"]
        player = Player.objects.get(player_id=player_id)
        return render(
            request,
            ScanView.template_name,
            context=ScanView.prepare_context_data(player)
        )

    @staticmethod
    @is_player
    def post(request):
        location = Location.get_from_QR(request.POST["qr_content"])
        # Is a valid QR code
        if location is not None:
            player = Player.objects.get(player_id=request.session["player_id"])
            item = location.get_item()
            respond = redirect('location', location_name=location.name.replace(" ", "_"))
            # if a new item was added
            # Add a new get variable to display a success message in the next view
            if player.add_item(item):
                respond = add_get_variables(respond, added="true")
            else:
                respond = add_get_variables(respond, added="false")
            return respond

        # Is not a valid QR code
        else:
            respond = redirect('scan')
            # add a get variable to display invalid qr
            # TODO mostrar mensaje de success
            respond = add_get_variables(respond, error="noqr")
            return respond


class MapView(View):
    """
    GET: render a UTFSM's map, display player's position.
    # TODO: Definir si usar un mapa de verdad usando la ubicación
    """
    template_name = 'player/map.html'

    @staticmethod
    @basic_context_data
    def prepare_context_data(player):
        ctx = {
            'player_id': player.player_id,
            'player': player,
        }
        return ctx

    @staticmethod
    @is_player
    def get(request):
        player_id = request.session["player_id"]
        player = Player.objects.get(player_id=player_id)
        return render(
            request,
            MapView.template_name,
            context=MapView.prepare_context_data(player)
        )


class CongratulationsView(View):
    """
    GET: You Won!
    """

    template_name = 'player/congratulations.html'

    @staticmethod
    @basic_context_data
    def prepare_context_data():
        return {}

    @is_player
    def get(self, request):
        # TODO determinar si efectivamente el jugador ha ganado
        return render(
            request,
            CongratulationsView.template_name,
            context=self.prepare_context_data
        )


class LocationView(View):
    """
    GET: display item, information about the place and the collectible
    """
    template_name = 'player/location.html'

    @staticmethod
    @basic_context_data
    def prepare_context_data(location, content):
        ctx = {
            "location": location,
            "location_name": location.name.title(),
            "content": content,
            "content_title": content.title.title(),
        }
        return ctx

    @staticmethod
    @is_player
    def get(request, location_name):
        location = Location.get_from_name(location_name)

        # valid location name
        if location:
            # check if user already scan its qr code
            player_id = request.session["player_id"]
            player = Player.objects.get(player_id=player_id)

            if player.has_location(location):
                # show location and item
                content = location.get_content()
                return render(
                    request,
                    LocationView.template_name,
                    context=LocationView.prepare_context_data(location, content)
                )
        # invalid location name or player didn't scan qr code yet
        respond = redirect("player")
        # TODO mostrar mensaje de error
        respond = add_get_variables(respond, error="loc")
        return respond
