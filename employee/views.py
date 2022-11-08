from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Employee, Profile
from django.template import loader
from django.urls import reverse

# Create your views here.
def employee_list(request):
	employees = Employee.objects.all()
	context = {
		'employees': employees
	}
	return render(request, 'employee/list.html', context)

def create_employee(request):
	if request.method == 'POST':
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		newEmp = Employee(first_name=first_name, last_name=last_name)
		newEmp.save()
		return HttpResponseRedirect(reverse('employee:employee_list'))
	else:
		template = loader.get_template('employee/create.html')
		return HttpResponse(template.render({}, request))

def edit_employee(request, pk):
	if request.method == 'POST':
		emp = Employee.objects.get(pk=pk)
		profile = Profile.objects.get(employee=emp)
		email = request.POST.get('email')
		age = request.POST.get('age')
		phone = request.POST.get('phone')
		address = request.POST.get('address')
		profile.email = email
		profile.phone = phone
		profile.address = address
		profile.age = age
		profile.save()
		return HttpResponseRedirect(reverse('employee:employee_list'))
	else:
		emp = Employee.objects.get(pk=pk)
		profile = Profile.objects.get(employee=emp)
		context = {
			'employee': emp,
			'profile': profile
		}
		return render(request, 'employee/edit.html', context)

def del_employee(request, pk):
	emp = Employee.objects.get(pk=pk)
	emp.delete()
	return HttpResponseRedirect(reverse('employee:employee_list'))
