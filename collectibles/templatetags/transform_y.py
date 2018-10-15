from django import template
from ..models import Location

register = template.Library()


@register.filter
def transform_y(value):
    try:
        return int((100 * int(value) + 5) / int(Location.MAX_X))
    except (ValueError, ZeroDivisionError):
        return None