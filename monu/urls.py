from django.urls import path
from monu import views

urlpatterns = [
    path('vehicle/create', views.create_vehicle_view, name='create_vehicle'),
    path('service/create', views.create_service_view, name='create_service'),
]
