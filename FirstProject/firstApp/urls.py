from django.urls import path
from firstApp import views

urlpatterns = [
    path('', views.users, name='users'),
]