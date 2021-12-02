# TODO: Create new routes for the requests
from django.urls import path
from . import views

urlpatterns = [
    path(
        "forum/comments",
        views.CommentByForum.as_view(),
        name="child-vaccine-log",
    ),

]
