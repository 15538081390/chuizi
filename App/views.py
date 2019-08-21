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
    products = Merchandise.objects.all()
    home=Indexhome.objects.all()
    tab=IndexTab.objects.all()
    a=[]
    c=[]
    for h in home:
        for p in products:
            if p.show==h.hid:
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
    bankuai = Productcategorie.objects.get(pcid=dise.show)            #需要修改查询条件，
    bankuai01 = Productcategorie.objects.filter(hid=dise.show)#查询相关商品
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
    pcmoney = round(dise.money * 0.7,2)#保留两位小数
    return render(request,"App/shopping/shop.html",locals())

def change(request):

    v1=request.POST['v1']
    v2=request.POST['v2']
    v3=request.POST['v3']
    v4=request.POST['v4']
    v5=request.POST['v5']
    product=request.POST['product']

    tab = IndexTab.objects.all()
    home = Indexhome.objects.all()
    dise=Merchandise.objects.filter(size=v1,capacity=v2,color=v3,specification=v4,kuanshi=v5,pcid=product).all()

    dise=dise[0]

    bankuai = Productcategorie.objects.get(pcid=dise.show)  # 需要修改查询条件，
    bankuai01 = Productcategorie.objects.filter(hid=dise.show)  # 查询相关商品
    color = Merchandise.objects.values("color").filter(pcid=dise.pcid).annotate(Count("pcid"))  # 颜色
    size = Merchandise.objects.values("size").filter(pcid=dise.pcid).annotate(Count("pcid"))  # 尺码
    kuanshi = Merchandise.objects.values("kuanshi").filter(pcid=dise.pcid).annotate(Count("pcid"))  # 款式
    capacity = Merchandise.objects.values("capacity").filter(pcid=dise.pcid).annotate(Count("pcid"))  # 容量
    specification = Merchandise.objects.values("specification").filter(pcid=dise.pcid).annotate(Count("pcid"))  # 规格
    pcmoney = round(dise.money * 0.7, 2)  # 保留两位小数
    return render(request,'App/shopping/change.html',locals())
    # return HttpResponse('xxxx')


def joinshopcar(request):
    if request.session.get('username'):
        mid=int(request.POST['mid'])
        product=Merchandise.objects.filter(mid=mid)
        user=User.objects.filter(username=request.session.get('username'))
        car1=Shopping(uid=user[0].uid,mid=mid,picture=product[0].picture,name=product[0].mername,price=product[0].money)
        car1.save()
        return HttpResponse('成功加入')
    else:

        return HttpResponse('请先登录')

def deletecar(request):
    id=request.POST['value']

    Shopping.objects.filter(sid=id).delete()
    user=User.objects.filter(username=request.session.get('username'))
    shopcar = Shopping.objects.filter(uid=user[0].uid)
    return render(request,'operate/delete.html',locals())

def pay1(request,mid):
    if request.session.get('username'):
        product=Merchandise.objects.get(mid=mid)

        addrs=Getaddr.objects.filter(username=request.session['username'])
        tab = IndexTab.objects.all()

        return render(request,'App/shopping/pay1.html',locals())
    else:
        return render(request,'operate/login11.html')

def save(request):
    if len(request.POST['phone'])==11:
        addr=Getaddr(username=request.session['username'],name=request.POST['name'],phone=request.POST['phone'],fulladdr=request.POST['addr'],street=request.POST['code'])
        addr.save()

        return HttpResponse('保存成功')
    else:
        return HttpResponse('请输入正确格式')

def deleteaddr(request):
    id=request.POST['id']
    print (id)
    Getaddr.objects.get(gid=id).delete()
    return HttpResponse('删除成功')

