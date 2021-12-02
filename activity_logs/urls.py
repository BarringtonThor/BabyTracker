from django.urls import path
from . import views

urlpatterns = [
    path(
        "child/vaccine-records",
        views.VaccinationLogsByChild.as_view(),
        name="child-vaccine-log",
    ),
    path(
        "child/sleep-records",
        views.SleepLogsByChild.as_view(),
        name="child-vaccine-log",
    ),
    path(
        "child/diaper-records",
        views.DiaperLogsByChild.as_view(),
        name="child-vaccine-log",
    ),
    path(
        "child/growth-records",
        views.GrowthLogsByChild.as_view(),
        name="child-vaccine-log",
    ),
    path("user/children", views.ChildrenByUser.as_view(), name="children-by-user"),
]
