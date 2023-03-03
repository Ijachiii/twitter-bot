from django.urls import path
from .views import *
from rest_framework.authtoken import views

urlpatterns = [
    path("", CheckAccountAPI.as_view(), name="check-account-api"),
    path("get-details/", UserDetailAPI.as_view()),
    # path("register/", RegisterUserAPI.as_view()),
    # path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'), 
]