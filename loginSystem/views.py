from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView 
from django.http import JsonResponse
from rest_framework.decorators import api_view, renderer_classes
# Create your views here.

#1) check phone no in
#2) 
otp_var = '123456'

@api_view(['POST'])
def user_enter_phoneno(request):
    phoneno = request.POST.get('phoneno', '')
    return Response({'status': 'success', 'result': otp_var})

@api_view(['POST'])
def verify_otp(request):
    phoneno = request.POST.get('phoneno', '')
    otp = request.POST.get('otp', '')
    # verify new user / old
    if otp == otp_var:
        response = Response({'status': 'success', 'result': "authencated"})
    else:
        response = Response({'status': 'failed', 'result': "not auth"})
    return response



@api_view(['POST'])
def fetch_profile(request):
    phoneno = request.POST.get('phoneno', '')
    return Response({'status': 'success', 'result': otp_var})
