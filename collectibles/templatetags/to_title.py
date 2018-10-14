from django import template

register = template.Library()


@register.filter
def to_title(value):
    return value.title()