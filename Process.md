DjangoWebApp/
    DjangoWebApp/
        __init__.py --空文件
        settings.py --主配置文件
        urls.py --主路由文件
        wsgi.py --网关接口
    templates/ --存放HTML文件安置目录
    manage.py --项目管理脚本
    login/ --APP
        admin.py --网站后台管理相关的文件
        apps.py --
        models.py --设计和表对应的类，模型类
        tests.py --写测试代码的文件
        views.py --定义处理函数，视图函数


ORM框架
    Object：对象-类
        图书类
    Mapping：映射
    Relations：关系，关系数据库中的表
####通过类和对象操作对应的数据表，不需要写sql语句    


模型类生成表
    1、生成迁移文件
        命令：python manage.py makemigrations
    2、执行迁移生成表
        命令：python manage.py migrate


后台管理
    1、本地化
        修改setting.py文件（语言和时间）
    2、创建管理员
        命令：python manage.py createsuperuser
    3、注册模型类
        在应用下的admin.py中注册模型类。
        告诉django框架根据注册的模型类来生成对应表管理页面
    4、自定义管理页面
        自定义**模型管理类**。模型管理类就是告诉django在生成的管理页面上显示哪些内容。
    
        
视图函数的使用
    1、定义视图函数
        视图函数定义在views.py中。
    2、进行url配置
    
    
模板
    1、创建模板文件夹
    2、配置模板目录
    3、使用模板文件
        a、加载模板文件
            取模板目录下获取html文件内容，得到一个模板对象
        b、定义模板上下文
            向模板文件传递数据。
        c、模板渲染
            得到一个标准的html文件




















    





