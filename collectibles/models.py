from django.db import models
from django.conf import settings
from random import choices


# Auxiliary functions
def key_generator():
    """Generate a qr key"""
    return "".join(choices(settings.QR_LOCATION_ENCODE["chars"], k=settings.QR_LOCATION_ENCODE["length"]))


# Create your models here
class Location(models.Model):
    """
    Location is a places in the real world where the QR code is. It has items and a content.
    """
    # unique QR key to generate a QR code
    QR_key = models.CharField(max_length=settings.QR_LOCATION_ENCODE["length"], unique=True, primary_key=True,
                              default=key_generator)

    # description of where the location is
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=124)

    def get_an_item(self):
        "return an random item"
        # TODO
        pass

    def get_QR(self):
        "generate a QR image"
        # TODO
        pass

    def __str__(self):
        return self.description


class Content(models.Model):
    """
    Content is the relevant information attached to a Location
    It can be an information page, an image or maybe a url
    """

    CONTENT_TYPES = (
        ("URL", "Url content"),
        ("IMG", "Image"),
        ("INFO", "Information")
    )
    # The name of the content
    title = models.CharField(max_length=120, null=False)

    # A short description of the content
    description = models.TextField(max_length=50)

    # It´s different to any content type
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    content = models.TextField()

    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)

    def render(self):
        "Generate the content corresponding to the content's type"
        # TODO
        pass

    def __str__(self):
        return self.title


class Item(models.Model):
    """
    Item is a collectible, it has a unique QR key to generate QR
    """
    name = models.CharField(max_length=124, unique=True)

    # TODO: Podemos usar coordenas si es que hay tiempo, por ahora solo una descripcion
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Player(models.Model):
    """
    Player is a player, use cookie session system, it has an unique player id to identify it.
    """

    # unique player id
    player_id = models.CharField(max_length=settings.ID_PLAYER_ENCODE["length"], unique=True, primary_key=True)
    nick = models.CharField(max_length=15)
    nick_suffix = models.CharField(max_length=5)
    active = models.BooleanField(default=True)

    @classmethod
    def create(cls, nick, check=False):

        nick_suffix = "".join(choices("1234567890", k=5))
        player_id = "".join(choices(settings.ID_PLAYER_ENCODE["chars"], k=settings.ID_PLAYER_ENCODE["length"]))

        while(check):
            # TODO revisar si ya existe el id en la BD
            check = False

        new_player = cls(player_id=player_id, nick=nick, nick_suffix=nick_suffix)
        return new_player


    def add_item(self, item):
        "add the item to the collection"
        # TODO
        pass

    def get_items(self):
        "return how many items it has and the items"
        # TODO
        pass

    def get_QR(self):
        "generate a QR image"
        # TODO
        pass

    def __str__(self):
        return f"{self.nick}::{self.nick_suffix}"


class AcquiredItem(models.Model):
    """
    Adquired item by a player
    """
    acquired_date = models.DateField(auto_now_add=True)

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f"{str(self.player)}::{str(self.item)}"
