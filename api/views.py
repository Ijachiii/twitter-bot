from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import AccountCheckedSerializer


# Create your views here.

@api_view(["POST"])
def checkAccount(request):
    serializer = AccountCheckedSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer["screen_name"])

    return Response(serializer.data)

