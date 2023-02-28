from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import AccountCheckedSerializer
from .demo import prediction


# Create your views here.

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

