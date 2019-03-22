# 网站后台管理相关的文件
# 建立应用和项目之间的联系，需要对应用进行注册

from django.contrib import admin
from login.models import UserInfo


# 自定义模型管理类
class UserInfoAdmin(admin.ModelAdmin):
    '''用户模型管理类'''
    list_display = ['user', 'pwd']


admin.site.register(UserInfo, UserInfoAdmin)

# Register your models here.
# 注册模型类
# admin.site.register(UserInfo)










