from django.urls import path
from .views import HomePageView, ResultView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"), 
    path("result/", ResultView.as_view(), name="result")
]