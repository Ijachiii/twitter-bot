from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import AccountCheckedSerializer, UserSerializer
from .demo import prediction


# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer


@api_view(["POST"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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

