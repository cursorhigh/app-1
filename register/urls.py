from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.register),
    path('rotp',views.register,name='reg'),
    path('votp',views.otpchk),
]