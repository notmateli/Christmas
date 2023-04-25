
from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages
# Create your views here.
# def crud(request):
# return render(request, 'crud.html')
def crud(request):
    data = Student.objects.all()
    print(data)
    # context = {"data": data}
    # return render(request, "crud.html", context)
    return render(request, "crud.html", {
        "data": data
    })
def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        # print(name, email, age, gender)
        query = Student(name=name, email=email, age=age, gender=gender)
        query.save()
        messages.info(request, "Data Inserted Successfully")
        return redirect("/crud")
    return render(request, 'crud.html')



