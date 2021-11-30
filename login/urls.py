from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("activate/<slug:uidb64>/<slug:token>/", views.activate, name="activate"),
    path("user/current", views.CurrentUserView.as_view(), name="logged-in-user"),
]
