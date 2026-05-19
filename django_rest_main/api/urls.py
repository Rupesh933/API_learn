from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeesViewset, basename='employees')

urlpatterns = [
    path(
        '', views.student
    ),
    path('singleStudent/<int:pk>/', views.singleStudentViewDetails),

    # class based url
    # path('employees/', views.EmployeesList.as_view()),
    # path('employees/<int:pk>/', views.SingleEmployee.as_view()),
    path('', include(router.urls)),


    path('comments/', views.CommentView.as_view()),
    path('blogs/', views.BlogViews.as_view()),
    path('comments/<int:pk>/', views.CommentDetailsView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailsView.as_view()),
]
