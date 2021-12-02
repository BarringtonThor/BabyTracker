"""babyTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework import routers

import activity_logs
from blogs import views as blog_views
from forum import views as forum_views
from activity_logs import views as activity_log_views

router = routers.DefaultRouter()
router.register(r"blogs", blog_views.BlogViewSet)
router.register(r"forum", forum_views.ForumViewSet)
router.register(r"comment", forum_views.CommentViewSet)
router.register(r"activity", activity_log_views.ActivityViewSet)
router.register(r"children", activity_log_views.ChildrenViewSet)
router.register(r"vaccine", activity_log_views.VaccinationLogsViewSet)
router.register(r"growth", activity_log_views.GrowthLogsViewSet)
router.register(r"sleep", activity_log_views.SleepLogsViewSet)
router.register(r"diaper", activity_log_views.DiaperChangeLogsViewSet)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("api.urls")),
    path("api/v1/", include("login.urls")),
    path("", include(router.urls)),
    path("", include("activity_logs.urls")),
    path("",include("forum.urls"))
]
