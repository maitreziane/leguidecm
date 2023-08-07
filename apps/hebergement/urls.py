from django.urls import path
from . import views


urlpatterns = [
    path('', views.Hebergement_view, name='hebergement' ), 
]