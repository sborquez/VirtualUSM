from django import template

register = template.Library()


@register.filter
def cut(value):
    if len(value) > 55:
        return value[:55]+"..."
    else:
        return value