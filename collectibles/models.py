from django.db import models


# Create your models here
class Content(models.Model):
    CONTENT_TYPES = (
        ("URL", "Url content"),
        ("IMG", "Image"),
        ("INFO", "Information")
    )
    title = models.CharField(max_length=120, null=False)
    description = models.TextField()

    # It´s different to any content type
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    content = models.TextField()


class Item(models.Model):
    """
    Item is a collectible, it has a unique QR key to generate QR
    """
    QR_key = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=124, unique=True)

    # TODO: Podemos usar coordenas si es que hay tiempo, por ahora solo una descripcion
    location = models.TextField(max_length=124)
    content = models.ForeignKey(Content, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Player(models.Model):
    """
    Player is a player, use cookie session system, it has an unique player id to identify it.
    """
    # unique player id
    player_id = models.CharField(max_length=64, unique=True)
    nick = models.CharField(max_length=25)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f"{self.nick}::{self.player_id}"

    def add_item(self, item):
        "add the item to the collection"
        # TODO
        pass

    def get_items(self):
        "return how many items it has and the items"
        # TODO
        pass
