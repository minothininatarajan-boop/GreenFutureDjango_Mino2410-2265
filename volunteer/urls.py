from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('register/', views.register),
    path('about/', views.about),
   path('create-admin/', views.create_admin),
]

