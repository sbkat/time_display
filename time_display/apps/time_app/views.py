from django.shortcuts import render, HttpResponse
from time import localtime, strftime

# Create your views here.

def index(request):
    context = {
        "time": strftime("%B %d, %Y %I:%M %p", localtime())
    }
    return render(request, 'time_app/index.html', context)