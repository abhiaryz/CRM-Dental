
from django.contrib import admin
from django.urls import path
from .views import user_enter_phoneno,verify_otp
urlpatterns = [
    path('phoneno/', user_enter_phoneno),
    path('verify_otp/', verify_otp),
]
