from django.db import models

# Create your models here.
#首页顶端模块表
class IndexTab(models.Manager):
    tid = models.AutoField(primary_key=True)                #首页顶端模块
    tname = models.CharField(max_length=128,unique=True)    #首页顶端模块名
    class Meta:
        db_table = "index_tab"

#首页选项表
class IndexHome(models.Manager):
    hid = models.AutoField(primary_key=True)               #首页选项ID
    gname = models.CharField(max_length=128,unique=True)   #首页选项名字
    class Meta:
        db_table = "indexhome"                              #表名

#首页分类表
class IndexCopy(models.Manager):
    cid = models.AutoField(primary_key=True)                #首页选项下的分类
    hid = models.IntegerField()                             #首页选项ID，表链接关键字
    cname = models.CharField(max_length=128,unique=True)    #分类名字
    class Meta:
        db_table = "indexcopy"                              #表名

#首页产品细分表
class IndexProduct(models.Manager):
    pid = models.AutoField(primary_key=True)                #首页产品细分表
    pname = models.CharField(max_length=128,unique=True)    #首尔产品细分名字
    cid = models.IntegerField(default=0)                    #首页分类表ID，表连接关键字
    class Meta:
        db_table ="indexproduct"                            #表名

#产品表
class ProductCategorie(models.Manager):
    pcid = models.AutoField(primary_key=True)               #产品id
    pcname = models.CharField(max_length=256,unique=True)   #产品名字
    pid = models.IntegerField()                             #首页产品细分类ID
    money = models.IntegerField()                           #价格
    inf = models.CharField(max_length=256)                  #产品文字说明说明
    image = models.CharField(max_length=256)                #产品信息图片
    # infimage=
    class Meta:
        db_table ="productcategorie"                        #产品表名


