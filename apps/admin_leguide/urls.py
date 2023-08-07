from django.urls import path
from . import views

urlpatterns = [
    path('Index-admin/', views.StartIndex_admin , name='StartIndex_admin' ),
    path('add_product/', views.add_product , name='add_product' ),
    path('add_attraction/', views.add_attraction , name='add_attraction' ),
    path('add_hebergement/', views.add_hebergement , name='add_hebergement' ),
    
]