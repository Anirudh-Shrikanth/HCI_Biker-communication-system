from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<str:user>/<str:chat_room>/', views.home),
    path('<str:user>/<str:chat_room>/record/', views.voice.as_view()),
]