
from django.shortcuts import render


# Create your views here.

def crud(request):
    return render(request, 'crud.html', {
    })
