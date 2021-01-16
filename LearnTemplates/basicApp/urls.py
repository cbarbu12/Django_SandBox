from django.urls import path, include
from basicApp import views


# Template tagging
app_name = 'basicApp'

urlpatterns = [
    path('relative', views.relative, name='relative'),
    path('other', views.other, name='other'),
]