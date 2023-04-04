from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


from django.http import HttpResponse

import datetime


def chris(request):
    now = datetime.datetime.now()
    return render(request, 'christmas.html', {
          "new": now.month == 12 and now.day == 25
    })
