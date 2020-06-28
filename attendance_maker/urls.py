from django.urls import path
from . import views

urlpatterns=[
    path('verifyFace',views.face_Verification,name='verifyFace'),
    path('teachers_desk',views.for_teachers,name='teachers_desk'),
    path('students_desk',views.for_students,name='students_desk'),
    path('location',views.send_response,name='send_response'),
    path('location_stud',views.send_response2,name='send_response2'),
    ]