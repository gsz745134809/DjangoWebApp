# 写 和数据库项目相关的内容
# 设计和表对应的类，模型类

from django.db import models

# Create your models here.

class UserInfo(models.Model):  # 要继承这个类，固定写法
    user = models.CharField(max_length=32)  # 创建两个字段，最大长度32，类型是char
    pwd = models.CharField(max_length=32)

class BookInfo(models.Model):
    '''图书模型类'''
    pass








