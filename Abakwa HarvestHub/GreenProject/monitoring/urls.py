from django.urls import path
from . import views

urlpatterns = [
    path('createfarm/', views.createFarm, name="create_farm"),
]
