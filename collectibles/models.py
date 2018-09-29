from django.db import models
from django.conf import settings
from random import choices


# Create your models here
def key_generator():
    return "".join(choices(settings.QR_LOCATION_ENCODE["chars"], k=settings.QR_LOCATION_ENCODE["length"]))

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


def id_generator():
    "generate an unique new player id"
    return "".join(choices(settings.ID_PLAYER_ENCODE["chars"], k=settings.ID_PLAYER_ENCODE["length"]))


class Player(models.Model):
    """
    Player is a player, use cookie session system, it has an unique player id to identify it.
    """

    # unique player id
    player_id = models.CharField(max_length=settings.ID_PLAYER_ENCODE["length"], unique=True, primary_key=True,
                                 default=id_generator)

    nick = models.CharField(max_length=25)

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
        return f"{self.nick}::{self.player_id}"


class AcquiredItem(models.Model):
    """
    Adquired item by a player
    """
    acquired_date = models.DateField(auto_now_add=True)

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f"{str(self.player)}::{str(self.item)}"
