from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponse
from events.models import Event


def index(request):
    events = Event.objects.all()
    context = {
        "title" : "Events App",
        "events" : events
    }
    return render(request,'index.html',context)

# Create your views here.
