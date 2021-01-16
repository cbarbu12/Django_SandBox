from django.urls import path, include
from basicApp import views

#template urls
app_name = 'basicApp'
urlpatterns = [
    path('register', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login')
]