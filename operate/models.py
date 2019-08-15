
from django.db import models

# Create your models here.

# 用户表
class User(models.Model):
    uid = models.AutoField(primary_key=True)                         #用户ID
    username = models.CharField(unique=True, max_length=50)          #用户名
    password = models.CharField(max_length=128)                      #密码
    phone = models.IntegerField(unique=True)                         #电话号码
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
    picture=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    price=models.IntegerField()


    class Meta:
        db_table = "shopcar"



#产品规格表
class Merchandise(models.Model):
    mid = models.AutoField(primary_key=True)                            #id
    pcid = models.IntegerField()                                        # 手机产品id
    mername = models.CharField(max_length=45)                           #手机名字
    money = models.FloatField()                                         #价格
    color = models.CharField(max_length=128,null=True)                  #颜色
    specification = models.CharField(max_length=128,null=True)          #规格
    size = models.CharField(max_length=128,null=True)                   #尺码
    capacity = models.CharField(max_length=128, null=True)              #容量
    xiaoliang = models.IntegerField(null=True)                          #销量
    kucun = models.IntegerField(default=10)                             #库存
    show = models.IntegerField()                                        #模板判断展示

    inf = models.CharField(max_length=45)                                # 产品说明
    picture = models.CharField(max_length=255, blank=True, null=True)    #主图片
    Choosepicture = models.CharField(max_length=255,null=True)           #颜色选择
    infpicture = models.CharField(max_length=255, blank=True, null=True) #产品说明图片


    class Meta:
        managed = False
        db_table = 'merchandise'







