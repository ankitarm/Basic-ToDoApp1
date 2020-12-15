from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('updatetask/<str:pk>', views.updateTask, name="updatetask"),
    path('delete/<str:pk>', views.delete, name="delete"),
]