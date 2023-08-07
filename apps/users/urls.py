from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.Register , name='register' ),
    path('login/', views.Login , name='login' ),
    path('Account_user/', views.Profil , name='profil' ),
    path('logout/', views.logout_view , name='logout' ),
]