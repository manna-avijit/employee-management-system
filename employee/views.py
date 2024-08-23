from django.shortcuts import render, redirect, HttpResponse
from .models import Employee, Department, Role
from django.db.models import Q


def index(request):
    return render(request, 'index.html')



def allEmp(request):
    data = Employee.objects.all()
    context = {'data': data, 'tot': len(data)}
    return render(request, 'allEmp.html', context)



def findEmp(request):
    emps = Employee.objects.all()
    if request.method == 'POST':
        empFilters = request.POST['empid']
       

        try:
            empFilters = int(empFilters)
            print(type(empFilters))
            data = emps.filter(id=empFilters)
            context = {'data': data}
            

        except:
            data = emps.filter(Q(firstName__icontains=empFilters) | Q(
                lastName__icontains=empFilters) | Q(dept__name__icontains=empFilters))
            context = {'data': data}
    else:
        context = {'data': emps}
    return render(request, 'findEmp.html', context)



def addEmp(request):
    if request.method == 'POST':
        firstname = (request.POST['first']).capitalize()
        lastname = (request.POST['last']).capitalize()
        phone = int(request.POST['phone'])
        jd = request.POST['date']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])

        
        newEmp = Employee(firstName=firstname, lastName=lastname, phone=phone,
                          salary=salary, bonus=bonus, hireDate=jd, dept=Department.objects.get(id=dept), role=Role.objects.get(id=role))
        newEmp.save()
        context = {'data': 1}
        return render(request, 'addEmp.html', context)

    return render(request, 'addEmp.html')


def rmEmp(request):
    emps = Employee.objects.all()
    if request.method == 'POST':
        empFilters = request.POST['empid']
        

        try:
            empFilters = int(empFilters)
            print(type(empFilters))
            data = emps.filter(id=empFilters)
            context = {'data': data}
           

        except:
            data = emps.filter(Q(firstName__icontains=empFilters) | Q(
                lastName__icontains=empFilters) | Q(dept__name__icontains=empFilters))
            context = {'data': data}
    else:
        context = {'data': emps}
    return render(request, 'rmEmp.html', context)



def updEmp(request, pk, status):
    
    data = Employee.objects.get(id=pk)
    context = {}
    if status == 0:
        context = {'data': data}
    elif status == 1:
        context = {'data': data, 'status': status}
    else:
        pass
    return render(request, 'updateEmp.html', context)



def delEmp(request, uid):
    print(uid)
    data = Employee.objects.get(id=uid)
    data.delete()
    return redirect(allEmp)



def dataUpEmp(request, id):
    
    if request.method == 'POST':
        data = Employee.objects.get(id=id)
        
        firstName = (request.POST['first']).capitalize()
        lastName = (request.POST['last']).capitalize()
        phone = int(request.POST['phone'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])

        data.firstName = firstName
        data.lastName = lastName
        data.phone = phone
        data.salary = salary
        data.bonus = bonus
        data.dept = Department.objects.get(id=dept)
        data.role = Role.objects.get(id=role)

        data.save()
       
        return redirect(updEmp, pk=id, status=1)
    else:
        return redirect(updEmp, pk=id, status=0)
