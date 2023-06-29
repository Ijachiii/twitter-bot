from django.urls import path
from .views import *
from rest_framework.authtoken import views
from drf_spectacular.views import (
SpectacularAPIView,
SpectacularRedocView,
SpectacularSwaggerView, 
)


urlpatterns = [
    path("", CheckAccountAPI.as_view(), name="check-account-api"),
    path("get-details/", UserDetailAPI.as_view()),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc",),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    # path("register/", RegisterUserAPI.as_view()),
    # path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'), 
]