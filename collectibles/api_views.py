from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Player, Location, Item, AcquiredItem


# from rest_framework import authentication, permissions
class PlayersList(APIView):
    """
    View to list all players in the system.

    """
    authentication_classes = []
    permission_classes = []

    @staticmethod
    def get(request):
        """
        Return a list of all users.

        Get params:
            all: (true|false) Show all players or hidden unactivated players, default false
            order: (items)|(created) Order the list by number of items or player created date
            q:  ([\d]+) Number of players
        """

        # Retrieve data
        try:
            q = int(request.GET.get("q", 0))
        except ValueError:
            q = 0

        show_all = request.GET.get("all", "false")
        order = request.GET.get("order", "created")

        # Filter active players
        if show_all == "true":
            players = Player.objects.all()
        else:  # show_all == "false"
            players = Player.objects.filter(active=True)

        # Order data
        if order == "created":
            players = players.order_by("created")

            # Preparing data
            players_list = []
            for player in players:
                players_list.append(
                    {
                        "nick": str(player),
                        "active": bool(player.active),
                        "items": player.acquireditem_set.count(),
                        "start_date": player.created
                    }
                )

        elif order == "items":
            # Preparing data
            players_list = []
            for player in players:
                players_list.append(
                    {
                        "nick": str(player),
                        "active": bool(player.active),
                        "items": player.acquireditem_set.count(),
                        "start_date": player.created
                    }
                )
            players_list = sorted(players_list, key=lambda p: p["items"], reverse=True)

        # Restring length
        if q > 0:
            players_list = players_list[:q]

        # Prepare Respond
        data = {
            "request": {
                "all": show_all,
                "order": order,
                "q": q,
            },

            "data": {
                "max_items": settings.CLIENT.locations,
                "total": len(players_list),
                "players": players_list,
            }
        }
        return Response(data)


class LocationsVisits(APIView):
    """
      View to list all locations in the system.
    """
    authentication_classes = []
    permission_classes = []

    @staticmethod
    def get(request):
        """
        Return a list of all locations.

        Get params:
            order: (players) Order the list by number of players visits
            q:  ([\d]+) Number of locations
        """

        # Retrieve data
        try:
            q = int(request.GET.get("q", 0))
        except ValueError:
            q = 0

        order = request.GET.get("order", None)

        locations = Location.objects.all()
        locations_list = []
        for location in locations:
            visits = location.get_visits()
            visits_list = [{"player": str(v.player), "item": str(v.item), "date": v.acquired} for v in visits]
            locations_list.append(
                {
                    "name": location.name,
                    "players": len(visits_list),
                    "visits": visits_list
                }
            )
        # Order data
        if order == "players":
            locations_list = sorted(locations_list, key=lambda l: l["players"])

        # Restring length
        if q > 0:
            locations_list = locations_list[:q]

        # Prepare Respond
        data = {
            "request": {
                "order": order,
                "q": q,
            },

            "data": {
                "total": len(locations_list),
                "locations": locations_list,
            }
        }
        return Response(data)


class PlayersVisits(APIView):
    """
      View to list all visits by players.
    """
    authentication_classes = []
    permission_classes = []

    @staticmethod
    def get(request):
        """
        Return a list of all items.

        Get params:
            q:  ([\d]+) Number of locations
        """

        # Retrieve data
        try:
            q = int(request.GET.get("q", 0))
        except ValueError:
            q = 0

        # Restring length
        if q > 0:
            #locations_list = locations_list[:q]
            pass

        # Prepare Respond
        data = {
            "request": {
                "q": q,
            },

            "data": {
            }
        }
        return Response(data)

"""
class PlayersItems(APIView):
    #View to list all items own by players.
    authentication_classes = []
    permission_classes = []

    @staticmethod
    def get(request):
        #Return a list of all items.

        #Get params:
        #    q:  ([\d]+) Number of locations
        

        # Retrieve data
        try:
            q = int(request.GET.get("q", 0))
        except ValueError:
            q = 0

        # Restring length
        if q > 0:
            #locations_list = locations_list[:q]
            pass

        # Prepare Respond
        data = {
            "request": {
                "q": q,
            },

            "data": {
            }
        }
        return Response(data)
"""
