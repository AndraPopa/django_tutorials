from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html", {"meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse("This pafe was served at " + str(datetime.now()))


def about(request):
    return HttpResponse("""Hi and welcome to my favourite page! 
                        It is supposed to display data about myself but neah""")


