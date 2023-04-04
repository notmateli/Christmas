from django.shortcuts import render


from django.http import HttpResponse

import datetime

def test(request):
    now = datetime.datetime
    return render(request, 'index.html', {
    "new": now.month == 1 and now.day == 1
    })



