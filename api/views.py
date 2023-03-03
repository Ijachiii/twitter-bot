from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView

from .serializers import *
from .demo import prediction


# Create your views here.
# class UserRegistrationView(generics.CreateAPIView):
#     serializer_class = UserSerializer


@api_view(["POST"])
def checkAccount(request):
    serializer = AccountCheckedSerializer(data=request.data)
    if serializer.is_valid():
        screen_name_ = serializer.data["screen_name"]
        pred = prediction(screen_name_)
        print(pred)
        seri = AccountCheckedSerializer(data={"screen_name": screen_name_, "prediction": pred})

        if seri.is_valid():
            seri.save()
        return Response(seri.data)

    return Response(serializer.data)

class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,SessionAuthentication)
  permission_classes = (IsAuthenticated,)
  def get(self,request,*args,**kwargs):
    user = get_user_model().objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (IsAuthenticated,)
  serializer_class = RegisterSerializer


# @permission_classes([IsAuthenticated])
# @authentication_classes([SessionAuthentication, BasicAuthentication])