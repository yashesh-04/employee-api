from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('employees/create/', views.create_employee),
    path('employees/', views.get_employees),
    path('employees/<int:id>/', views.get_single_employee),
    path('employees/delete/<int:id>/', views.delete_employee),
    path('employees/update/<int:id>/', views.update_employee),
    path('employees/<str:company>/', views.get_employees_by_company),
]