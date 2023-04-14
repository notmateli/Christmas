from django.shortcuts import render
from django import forms


# from django.forms import forms

# Create your views here.
class NewTaskForm(forms.Form):
    task = forms.CharField(label="Task Field")
    # phone = forms.IntegerField(label="Age", min_value="10", max_value="12")


class OldTaskForm(forms.Form):
    task = forms.CharField(label="Email")


tasks = ["Buy groceries", "Play games", "Watch Football"]


def test(request):
    return render(request, "tasks.html", {

        "Tasks": tasks

    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request, "add.html", {
                "form": form
            })

    return render(request, "add.html", {
        "form": NewTaskForm()
    })


def ongeza(request):
    return render(request, "ongeza.html", {
        "form": OldTaskForm()
    })
