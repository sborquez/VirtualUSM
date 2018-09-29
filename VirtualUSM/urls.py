"""VirtualUSM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.views.generic import RedirectView

from collectibles import admin_views

urlpatterns = [
    # Admins customs views
    path("admin/dashboard/", admin_views.dashboard, name="dashboard"),
    path("admin/print/", admin_views.print_menu, name="printer"),

    # Admin urls
    path('admin/', admin.site.urls),


    # Collectibles urls start with app/
    path('app', include('collectibles.urls')),

    # Redirect '/' to 'app/'
    path('', RedirectView.as_view(url='/app/', permanent=True))
]
