from django.conf.urls import url

from . import views
urlpatterns = [
    # Players views
    url(r"^/$", views.AboutView.as_view(), name="about"),
    url(r"^/start/?$", views.StartView.as_view(), name="start"),
    url(r"^/me/?$", views.PlayerView.as_view(), name="player"),
    url(r"^/scan/?$", views.ScanView.as_view(), name="scan"),
    url(r"^/map/?$", views.MapView.as_view(), name="map"),
    url(r"^/found/(?P<item_id>\d+)/?$", views.ItemView.as_view(), name="item"),
    url(r"^/congratulations/?$", views.CongratulationsView.as_view(), name="congrats"),

    # Admins views
    url(r"^/dashboard/?$", views.DashboardView.as_view(), name="dashboard"),
    url(r"^/print/?$", views.ItemsView.as_view(), name="printer"),
]


