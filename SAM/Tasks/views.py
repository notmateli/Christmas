from django.shortcuts import render

# Create your views here.

tasks = ["Buy groceries", "Play games", "Watch Football"]
def task(request):
    return render(request, "tasks.html", {

        "tasks": tasks

    })
