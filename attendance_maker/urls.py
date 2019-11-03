from django.urls import path
from . import views

urlpatterns=[
    path('teachers_desk',views.for_teachers,name='teachers_desk'),
    path('students_desk',views.for_students,name='students_desk'),
    
    
    ]