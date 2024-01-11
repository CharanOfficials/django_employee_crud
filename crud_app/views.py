from django.shortcuts import render
from crud_app.models import Tbl_Employee
from django.shortcuts import redirect
# Create your views here.


def create(request):
    if request.method == 'POST':
        e_name = request.POST.get('name')
        e_email = request.POST.get('email')
        e_mobile = request.POST.get('mobile')
        qs = Tbl_Employee.objects.create(
            name=e_name, email=e_email, mobile_no=e_mobile)
        if qs:
            return redirect('retrieve')
    else:
        return render(request, "create_emp.html")


def retrieve_all_emp(request):
    qs = Tbl_Employee.objects.all()
    return render(request, 'retrieve.html', context={'emp_data': qs})


def delete_emp(request, emp_id):
    qs = Tbl_Employee.objects.filter(id=emp_id).delete()
    if qs:
        return redirect('retrieve')


def update_emp(request, emp_id):
    if request.method == "POST":
        e_name = request.POST.get('name')
        e_email = request.POST.get('email')
        e_mobile = request.POST.get('mobile')
        qs = Tbl_Employee.objects.filter(id=emp_id).update(
            name=e_name, email=e_email, mobile_no=e_mobile)
        if qs:
            return redirect('retrieve')
    else:
        qs = Tbl_Employee.objects.get(id=emp_id)
        return render(request, 'update.html', context={'emp_data': qs})
