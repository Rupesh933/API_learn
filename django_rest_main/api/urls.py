from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(
        '', views.student
    ),
    path('singleStudent/<int:pk>/', views.singleStudentViewDetails),

    # class based url
    path('employee/', views.Employee.as_view()),
    path('employees/<int:pk>/', views.SingleEmployee.as_view()),
]
