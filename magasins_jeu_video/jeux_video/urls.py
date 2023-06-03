from django.urls import path

from . import views

from django.urls import path
from . import views
from . import livreviews

urlpatterns = [
    path('index/', views.index),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/', views.affiche),
    path('delete/<int:id>/', views.delete),
    path('update/<int:id>/', views.update),
]