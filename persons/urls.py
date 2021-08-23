from django.urls import path
from persons import views

urlpatterns = [
    path('student/create', views.student_create_view, name='create_student'),
    path('driver/create', views.driver_create_view, name='create_driver'),
]
