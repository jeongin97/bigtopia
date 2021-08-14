
from django.urls import path
from .import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about/',views.about, name='about'),
    path('activity/',views.activity, name='activity'),
    path('hire/',views.hire, name='hire'),
    path('studyroom/',views.studyroom, name='studyroom'),
    path('aboutX/', views.aboutX, name='aboutX'),

    path('post/',views.post),
    path('post/<int:id>', views.detail, name='detail'),
    path('post/update/', views.update, name='update'),
    path('post/update/<int:id>', views.update, name='update'),
    path('post/delete/<int:id>', views.delete, name='delete'),
    path('post/comment/<int:id>',views.comment,name='comment'),
    path('fail/', views.fail, name='fail'),
]

