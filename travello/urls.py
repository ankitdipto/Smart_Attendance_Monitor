from django.urls import path

from . import views

urlpatterns=[

    path('',views.index,name='project_index'),
    path('contact',views.contact,name='contact'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('record',views.record,name='record'),
    path('ViewClassRecord',views.record,name='record')
]

