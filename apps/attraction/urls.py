from django.urls import path
from . import views

urlpatterns = [
    path('', views.Attraction , name='attraction' ),]