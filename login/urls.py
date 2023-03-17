from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.login),
    path('log',views.login,name='log'),
    path('clog',views.otpver),
]