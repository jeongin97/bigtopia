
from django.urls import path
from.import views

urlpatterns=[
    path('exam3/', views.exam3, name='exam3'),
    path('main/', views.main, name='main'),
    path('exam15/', views.exam15, name='exam15'),
    path('homework2/', views.homework2, name='homework2')

]