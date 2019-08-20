# coding=utf-8
from urllib import request

from django.db.models import Count,Min,Max
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from App.models import *
from operate.models import *
import random

# Create your views here.
#首页
def index(request):
    products = Productcategorie.objects.all()
    home=Indexhome.objects.all()
    tab=IndexTab.objects.all()
    a=[]
    c=[]
    for h in home:
        for p in products:
            if p.hid==h.hid:
                a.append(p)
        if len(a)>8:
            a=random.sample(a,8)
            for a1 in a:
                c.append(a1)
            a=[]
        else:
            for a1 in a:
                c.append(a1)
            a=[]
    print(c)
    return render(request,"App/bash/bash.html",context={"home":home,
                                                        "tab":tab,
                                                        "products":c,
                                                        })


    # return HttpResponse("111111")

# 商品展示

def second(request,cid):
    home = Indexhome.objects.all()
    tab = IndexTab.objects.all()
    copy=Indexcopy.objects.all()
    indepro=Indexproduct.objects.all()
    pros=Merchandise.objects.values('pcid').annotate(Min('mid'))

    list1=[]
    for p in pros:
        list1.append(p['mid__min'])
    produ=Merchandise.objects.filter(mid__in=list1) #每类商品第一个

    return render(request,"App/bash/second.html",context={"home":home,
                                                        "tab":tab,
                                                        "products":produ,
                                                          "to_id":int(cid),
                                                          "copy":copy,
                                                          "indepro":indepro,})

#服务条款
def server(request):
    tab=IndexTab.objects.all()
    return render(request,"App/bash/server.html",context={"tab":tab,
                                                          })
#售后政策
def server2(request):
    tab=IndexTab.objects.all()
    return render(request,"App/bash/server2.html",context={"tab":tab,
                                                          })
#保修服务
def server3(request):
    tab=IndexTab.objects.all()
    home=Indexhome.objects.all()
    return render(request,"App/bash/server3.html",context={"tab":tab,
                                                           "home":home,
                                                          })
def application(request):
    tab=IndexTab.objects.all()
    return render(request,"App/topbash/app.html",context={"tab":tab,
                                                          })

def osx(request):
    tab=IndexTab.objects.all()
    return  render(request,"App/topbash/osx.html",context={"tab":tab,
                                                           })

def pron2s(request):
    tab=IndexTab.objects.all()
    return render(request,"App/topbash/pron2s.html",context={"tab":tab,
                                                        })
def r1(request):
    tab=IndexTab.objects.all()
    return render(request,"App/topbash/r1.html",context={"tab":tab,
                                                         })

def dingduan(request):
    tab=IndexTab.objects.all()
    return render(request,"App/topbash/dingduan.html",context={"tab":tab,
                                                          })
def tnt(request):
    tab=IndexTab.objects.all()
    return render(request,"App/topbash/tnt.html",context={"tab":tab,
                                                          })

#商品购买
def show(request,num):
    tab=IndexTab.objects.all()
    home = Indexhome.objects.all()
    dise = Merchandise.objects.get(mid=num)                     #从规格表查询产品表
<<<<<<< HEAD

    bankuai = Productcategorie.objects.get(pcid=dise.show)            #需要修改查询条件，
    bankuai01 = Productcategorie.objects.filter(hid=dise.show)#查询相关商品


=======
    bankuai = Productcategorie.objects.get(pcid=dise.show)            #需要修改查询条件，
    bankuai01 = Productcategorie.objects.filter(hid=dise.show)#查询相关商品

>>>>>>> a6bf5c97f513ec0e0177b776033f72b134ca3c74
    #规格查询
    color = Merchandise.objects.values('pcid',"color","Choosepicture").filter(pcid=dise.pcid).annotate(Count("pcid"))             #颜色
    size = Merchandise.objects.values("size").filter(pcid=dise.pcid).annotate(Count("pcid"))                   # 尺码
    kuanshi = Merchandise.objects.values("kuanshi").filter(pcid=dise.pcid).annotate(Count("pcid"))                   # 款式

    capacity = Merchandise.objects.values("capacity").filter(pcid=dise.pcid).annotate(Count("pcid"))            #容量
    specification = Merchandise.objects.values("specification").filter(pcid=dise.pcid).annotate(Count("pcid"))  #规格
    #查询商品
    # pc = Productcategorie.objects.get(pcid=dise.mid)
    num1=num  #商品id
    #折扣价格
<<<<<<< HEAD
    pcmoney = round(dise.money * 0.7,2)#保留两位小数

=======
    pcmoney = dise.money * 0.7
>>>>>>> a6bf5c97f513ec0e0177b776033f72b134ca3c74
    return render(request,"App/shopping/shop.html",locals())


def joinshopcar(request):
    if request.session.get('username'):
        pid=int(request.POST['pid'])
        product=Merchandise.objects.filter(pcid=pid)
        user=User.objects.filter(username=request.session.get('username'))
        car1=Shopping(uid=user.uid,mid=pid,picture=product.pricture,name=product.mername,price=product.money)
        car1.save()
        return HttpResponse('成功加入')
    else:
<<<<<<< HEAD
        return HttpResponse('请先登录')
=======
        return HttpResponse('请先登录')
>>>>>>> a6bf5c97f513ec0e0177b776033f72b134ca3c74
