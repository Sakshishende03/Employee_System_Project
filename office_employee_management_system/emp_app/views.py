from django.shortcuts import render
from emp_app.models import Employee
from django.http import HttpResponse
import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def all_emp(request):
    emp_list = Employee.objects.all()
    my_dict = {'emp_list':emp_list}
    return render(request,'testapp/all_emp.html',my_dict)




from datetime import datetime
from django.shortcuts import render, HttpResponse
from .models import Employee

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])  # Corrected this line
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        new_emp = Employee(first_name=first_name, last_name=last_name, dept_id=dept, salary=salary, bonus=bonus,
                           role_id =role, phone=phone, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Successfully!!')
    elif request.method == 'GET':
        return render(request, 'testapp/add_emp.html')
    else:
        return HttpResponse("An Exception Occurred!")

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Sucessfully!!")
        except:
            return HttpResponse("Please Enter A Valid Employee Id")

    emp_list = Employee.objects.all()
    my_dict = {'emp_list':emp_list}
    return render(request,'testapp/remove_emp.html',my_dict)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emp_list = Employee.objects.all()
        if name:
            emp_list = emp_list.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emp_list =emp_list.filter(dept__name = dept)
        if role:
            emp_list = emp_list.filter(role__name = role)

        my_dict = {'emp_list':emp_list}
        return render(request, 'testapp/all_emp.html',my_dict)

    elif request.method=='GET':
        return render(request,'testapp/filter_emp.html')

    else:
        return HttpResponse("An Exception Occurred!!")
