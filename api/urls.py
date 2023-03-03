from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", checkAccount, name="check-account-api"),
    path("get-details/", UserDetailAPI.as_view()),
    path("register/", RegisterUserAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
]