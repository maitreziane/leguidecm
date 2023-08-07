from django.urls import path
from . import views

urlpatterns = [
    path('', views.Product_view , name='product' ),]