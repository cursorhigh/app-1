from django.contrib import admin
from django.urls import path,include
from .import views
from .views import google_login_callback
#home
urlpatterns = [
    path('',views.home),
    path('download_page/',views.download_page),
    path('reg/',views.reg),
    path('logout/',views.logout),
    path('log/',views.log),
    path('sboard/',views.leaderboard),
    path('accounts/google/login/callback/', google_login_callback, name='google_login_callback'),

]
