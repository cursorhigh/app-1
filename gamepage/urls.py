from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.gpage),
    path('enable',views.roomon,name='enable'),
    path('<str:room>/', views.room, name='room'),
    path('disable',views.roomoff,name='disable'),
    path('join',views.join,name='join'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('', views.home, name='home'),
]