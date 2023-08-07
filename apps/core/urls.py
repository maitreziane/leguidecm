from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index , name='index' ),
    path('detail/<slug:category_slug>/<slug:id>', views.detailProduct , name='detailproduct' ),
    path('a-propros/', views.About, name='about' ),
]