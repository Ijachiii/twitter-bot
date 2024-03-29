"""twitter_bot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from twitterbot.views import signup, login

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    # path("accounts/login/", LoginView.as_view(), name="login"),
    path("api-auth/", include("rest_framework.urls")),
    path("accounts/signup/", signup),
    path("accounts/login/", login, name="login"),
    path("", include("twitterbot.urls")),
    path("api/", include("api.urls")),
    path("api/dj-rest-auth/", include("dj_rest_auth.urls")),
    path("api/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("oauth/", include("social_django.urls"))
    
]