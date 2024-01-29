from django.urls import path
from . import views

urlpatterns = [
    path('farm/', views.getFarmInfo, name="get_farm_info"),
    path('createfarm', views.createFarm, name="create_farm"),
]
