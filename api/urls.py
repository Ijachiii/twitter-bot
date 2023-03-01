from django.urls import path
from .views import *

urlpatterns = [
    path("", checkAccount, name="check-account-api"),
]