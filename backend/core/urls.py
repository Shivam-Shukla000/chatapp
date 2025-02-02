from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from .views import TestAPI, get_routes, MyTokenObtainPairView, RegisterView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('home/', TestAPI.as_view(), name='home'),
    path('', get_routes, name='api'),
]
