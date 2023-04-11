from django.shortcuts import render

# Create your views here.

tasks = ["Buy groceries", "Play games", "Watch Football"]
def test(request):
    return render(request, "tasks.html", {

    "Tasks": tasks

    })
def add(request):
    return render(request, "add.html")