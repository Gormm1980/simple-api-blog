from django.urls import path
from user.api.views import RegisterView,UserView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)



urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/me', UserView.as_view()),
]