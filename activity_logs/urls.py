from django.urls import path
from . import views

urlpatterns = [
    path(
        "child/vaccine-records",
        views.VaccinationLogsByChild.as_view(),
        name="token_obtain_pair",
    ),
]
