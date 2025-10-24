from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_student, name='add_student'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/<int:pk>/add_grade/', views.add_grade, name='add_grade'),
    path('order/', views.order_by_average, name='order_by_average'),
    path('search/', views.search_student, name='search_student'),
    path('undo/', views.undo_action, name='undo_action'),
]
