from django.db import models

# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from __future__ import unicode_literals
#
# from django.db import models

#畅呼吸商品类
class Breath(models.Model):
    idbreath = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)
    money = models.FloatField()
    picture = models.CharField(max_length=45, blank=True, null=True)
    infpicture = models.CharField(max_length=45, blank=True, null=True)
    infserver = models.CharField(max_length=45, blank=True, null=True)
    inf = models.CharField(max_length=45, blank=True, null=True)
    black = models.IntegerField()
    white = models.IntegerField()
    fuhe = models.IntegerField()
    jiaquan = models.IntegerField()
    biaozhun = models.IntegerField()
    xiaoliang = models.IntegerField()
    tochan = models.IntegerField()
    kucun = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'breath'

#衣服商品类
class Clothes(models.Model):
    idclothes = models.AutoField(primary_key=True)
    money = models.FloatField()
    name = models.CharField(max_length=45)
    picture = models.CharField(max_length=45, blank=True, null=True)
    infpicture = models.CharField(max_length=45, blank=True, null=True)
    inf = models.CharField(max_length=45, blank=True, null=True)
    infserver = models.CharField(max_length=45, blank=True, null=True)
    black = models.IntegerField()
    white = models.IntegerField()
    fifteen_6 = models.IntegerField()
    twenty = models.IntegerField()
    notopen = models.IntegerField()
    s = models.IntegerField()
    l = models.IntegerField()
    m = models.IntegerField()
    xl = models.IntegerField()
    man = models.IntegerField()
    kid = models.IntegerField()
    women = models.IntegerField()
    three_7 = models.IntegerField()
    three_8 = models.IntegerField()
    three_9 = models.IntegerField()
    four_0 = models.IntegerField()
    four_1 = models.IntegerField()
    four_2 = models.IntegerField()
    xiaoliang = models.IntegerField()
    tochan = models.IntegerField()
    kucun = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clothes'

#首页顶行
class IndexTab(models.Model):
    tid = models.AutoField(primary_key=True)
    tname = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'index_tab'

#选项表分类
class Indexcopy(models.Model):
    cid = models.AutoField(primary_key=True)
    hid = models.IntegerField()
    cname = models.CharField(max_length=45)
    indexcopycol = models.CharField(unique=True, max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indexcopy'

#选项表分类
class Indexhome(models.Model):
    hid = models.AutoField(primary_key=True)
    gname = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'indexhome'

#产品细分
class Indexproduct(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(unique=True, max_length=45)
    cid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'indexproduct'

#小件产品类
class Parts(models.Model):
    partsid = models.AutoField(primary_key=True)
    partsname = models.CharField(unique=True, max_length=45)
    money = models.FloatField()
    one = models.IntegerField()
    two = models.IntegerField()
    three = models.IntegerField()
    white = models.IntegerField()
    black = models.IntegerField()
    diantongban = models.IntegerField(blank=True, null=True)
    picture = models.CharField(max_length=45, blank=True, null=True)
    infpicture = models.CharField(max_length=45, blank=True, null=True)
    inf = models.CharField(max_length=45, blank=True, null=True)
    infserver = models.CharField(max_length=45, blank=True, null=True)
    xiaoliang = models.IntegerField()
    tochan = models.IntegerField()
    kucun = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'parts'

#手机产品类
class Phone(models.Model):
    idphone = models.AutoField(primary_key=True)
    phonename = models.CharField(max_length=45)
    picture = models.CharField(max_length=45, blank=True, null=True)
    infpicture = models.CharField(max_length=45, blank=True, null=True)
    inf = models.CharField(max_length=45)
    money = models.FloatField()
    white = models.IntegerField()
    black = models.IntegerField()
    six_64 = models.IntegerField()
    six_128 = models.IntegerField()
    eight_128 = models.IntegerField()
    eight_512 = models.IntegerField()
    gailan = models.CharField(max_length=45, blank=True, null=True)
    sheji = models.CharField(max_length=45, blank=True, null=True)
    gongneng = models.CharField(max_length=45, blank=True, null=True)
    xiaoliang = models.IntegerField()
    tochan = models.IntegerField()
    kucun = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phone'

#产品表
class Productcategorie(models.Model):
    pcid = models.AutoField(primary_key=True)
    pcname = models.CharField(unique=True, max_length=45)
    pid = models.IntegerField()
    hid = models.IntegerField()
    money = models.FloatField()
    inf = models.CharField(max_length=45)
    red = models.IntegerField()
    white = models.IntegerField()
    black = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'productcategorie'



