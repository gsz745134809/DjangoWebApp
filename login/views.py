# 接收请求，进行处理，与M和T进行交互，返回应答
# 定义处理函数，视图函数

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader, RequestContext
from login import models

# Create your views here.

# user_list = []

# 定义视图函数
def index(request):  # 第一个参数必须是request。request参数封装了用户请求的所有内容
    # return HttpResponse('hello world')  # 不能直接返回字符串，必须由这个类封装起来，才能被HTTP协议识别


    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        # temp = {'user': username, 'pwd': password}  # 将发送过来的用户名和密码构造成一个字典
        # user_list.append(temp)  # 将字典添加到列表里

        # 将数据保存到数据库
        models.UserInfo.objects.create(user=username, pwd=password)

    # 从数据库中读取所有数据，注意缩进
    user_list = models.UserInfo.objects.all()

    return render(request, 'index.html', {'data': user_list})  # render方法使用数据字典和请求元数据，渲染一个指定的HTML模板。其多个参数中，第一个参数必须是request，第二个是模板
    #  {'data': user_list} 将用户列表作为上下文参数供render渲染index页面


def index2(request):
    # 进行处理，和M及T进行交互
    # return HttpResponse('something')

    # 使用模板文件
    # 1、加载模板文件，模板对象
    temp = loader.get_template('login/index.html')
    # 2、定义模板上下文：给模板文件传递数据
    context = RequestContext(request, {})
    # 3、模板渲染：产生标准的html内容
    res_html = temp.render(context)
    # 4、返回给浏览器
    return HttpResponse(res_html)








