from urllib import request

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"App/bash/bash.html")
    # return HttpResponse("111111")