from django.urls import path
from rest_framework_simplejwt.views import (
    token_obtain_pair,
    token_refresh,
)

from .views import user_registration_serializer

app_name = 'users'

urlpatterns = [
    path('token/', token_obtain_pair, name='token_obtain_pair'),
    path('token/refresh/', token_refresh, name='token_refresh'),
    path('register/', user_registration_serializer, name='register'),
]
