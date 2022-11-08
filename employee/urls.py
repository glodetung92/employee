from django.urls import path, include
from .import views

app_name = 'employee'
urlpatterns = [
	path('', views.employee_list, name='employee_list'),
	path('create/', views.create_employee, name='create-employee'),
	path('edit/<int:pk>/', views.edit_employee, name='edit-employee'),
	path('delete/<int:pk>/', views.del_employee, name='del-employee'),
]
