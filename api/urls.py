from django.urls import include, path
from .views import base_view

urlpatterns = [
    path("", base_view, name="base view"),
]
