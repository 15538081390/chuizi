
from django.db import models

# Create your models here.

# 用户表
class User(models.Model):
    uid = models.IntegerField(primary_key=True, auto_created=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    phone = models.IntegerField(unique=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    safeqnum = models.IntegerField(blank=True, null=True)                   # 安全问题的序号
    answer = models.CharField(max_length=100, blank=True, null=True)        # 安全问题的答案

    class Meta:
        managed = False
        db_table = 'user'


class Getaddr(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    fulladdr = models.CharField(max_length=255, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    etc = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'getaddr'



