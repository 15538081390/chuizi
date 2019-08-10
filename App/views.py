from urllib import request

from django.http import HttpResponse
from django.shortcuts import render
from App.models import *

# Create your views here.

def index(request):
    home=Indexhome.objects.all()
    tab=IndexTab.objects.all()
    return render(request,"App/bash/bash.html",context={"home":home,
                                                        "tab":tab,})


    # return HttpResponse("111111")


def second(request,cid):
    home = Indexhome.objects.all()
    tab = IndexTab.objects.all()
    products=Productcategorie.objects.all()


    return render(request,"App/bash/second.html",context={"home":home,
                                                        "tab":tab,
                                                        "products":products,
                                                          "to_id":int(cid)})



