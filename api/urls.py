from django.urls import path
from .views import *

urlpatterns = [
    path("", checkAccount, name="check-account-api"),
    path("register/", UserRegistrationView.as_view(), name="user-reg")
]