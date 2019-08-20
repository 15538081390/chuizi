from django.db import models

# Create your models here.

# 用户表
class User(models.Model):
    uid = models.AutoField(primary_key=True)                         #用户ID
    username = models.CharField(unique=True, max_length=50)          #用户名
    password = models.CharField(max_length=128)                      #密码
    phone = models.CharField(unique=True, max_length=50)                         #电话号码
    email = models.CharField(max_length=100, blank=True, null=True)  #邮箱
    portrait = models.CharField(max_length=256,null=True)                      #头像
    safeqnum = models.IntegerField(blank=True, null=True)             # 安全问题的序号
    answer = models.CharField(max_length=100, blank=True, null=True)  # 安全问题的答案
    class Meta:
        db_table = 'user'

#收货地址
class Getaddr(models.Model):
    gid = models.AutoField(primary_key=True)
    uid = models.ImageField(null=True)
    username = models.IntegerField(null=True)                            # 用户id
    fulladdr = models.CharField(max_length=255, blank=True, null=True) #详细地址
    street = models.CharField(max_length=256,null=True)                 #街道地址
    phone = models.IntegerField(blank=True, null=True)            #手机号码
    etc = models.CharField(max_length=50, blank=True, null=True)  #默认地址
    telephone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'getaddr'

#购物清单表
class Orderform(models.Model):
    oid = models.AutoField(primary_key=True)         #订单id
    ordernumber = models.CharField(max_length=250,unique=True)   #订单号
    uid = models.IntegerField()                      #用户id
    pid = models.IntegerField()                     #商品id
    invoice = models.IntegerField(default=0)         #发票信息#0=个人1=单位
    emil = models.CharField(max_length=128,null=True) #判空默认发送账户邮箱
    number = models.IntegerField()                   #订单数量
    time = models.DateField()                        #订单时间

    class Meta:
        db_table = "orderform"
#购物车
class Shopping(models.Model):
    sid = models.AutoField(primary_key=True)         #购物车id
    uid = models.IntegerField()                      #用户id
    mid = models.IntegerField()                     #商品id
    picture=models.CharField(max_length=255,null=True)
    name=models.CharField(max_length=255,null=True)
    price=models.IntegerField()


    class Meta:
        db_table = "shopcar"









