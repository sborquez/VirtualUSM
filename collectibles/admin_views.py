from django.shortcuts import render, redirect
from django.conf import settings

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required

from .models import Location

# Admin's Views
dashboard_template = 'admin/dashboard.html'
print_template = 'admin/print.html'


def get_context_data(**kwargs):
    ctx = {
        'str_app': settings.CLIENT.app,
        "bool_show_ctx": settings.DEBUG,
        **kwargs
    }
    return ctx


def dashboard(request):
    """
    Get: display a report of game
    """
    return render_to_response(
        dashboard_template,
        get_context_data(),
        RequestContext(request, {})
    )


def print_menu(request):
    """
    Get: display a GUI to print item's QR
    """

    locations = Location.objects.all()

    size = int(request.GET.get("cm", 6))

    return render_to_response(
        print_template,
        get_context_data(locations=locations, size=size),
        RequestContext(request, {})
    )


print_menu = staff_member_required(print_menu)
dashboard = staff_member_required(dashboard)
