from nturl2path import url2pathname
from django.urls import path
from catdog_ai import views

urlpatterns = [
    path('pet/', views.PetView.as_view()),
]