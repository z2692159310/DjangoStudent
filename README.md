# Django-Student

### 介绍
  Django 实现学生后台管理系统

### 软件架构
  Python3.7+Django2.2+Xadmin2 实现学生后台管理系统


### 安装教程
#### 1. 配置Python3.6(及以上)的虚拟环境

#### 2. 装包

+ 安装运行所需的包	

  ```python
  # 安装Django
  pip install Django==2.2
  # 安装xadmin
  pip install https://codeload.github.com/sshwsfc/xadmin/zip/django2
  # 安装上传图片所需的包
  pip install Pillow
  ```

+ 镜像使用：

  > https://blog.csdn.net/sinat_21591675/article/details/82770360

#### 3. 启动服务

+ 进入“终端”CMD命令，进入项目apps文件夹

  ```python
  cd apps
  ```

+ 启动服务

  ```python
  python manage.py runserver
  ```
  

### 4. <font color="red">报错</font>

+ 出现下面错误

  ```sh
  Traceback (most recent call last):
    File "manage.py", line 21, in <module>
      main()
    File "manage.py", line 17, in main
      execute_from_command_line(sys.argv)
    File "D:\git\PythonProjects\DjangoStudent\venu\lib\site-packages\django\core\ma
  nagement\__init__.py", line 381, in execute_from_command_line
      utility.execute()
      
  ...
  
  # 注意看下面这个文件路径
    File "D:\git\PythonProjects\DjangoStudent\venu\lib\site-packages\xadmin\plugins
  \importexport.py", line 48, in <module>
      from import_export.admin import DEFAULT_FORMATS, SKIP_ADMIN_LOG, TMP_STORAGE_
  CLASS
  ImportError: cannot import name 'SKIP_ADMIN_LOG' from 'import_export.admin' (D:\g
  it\PythonProjects\DjangoStudent\venu\lib\site-packages\import_export\admin.py)
  
  ```

+ 找到虚拟环境下的包所在的路径，我的是 `D:\git\PythonProjects\DjangoStudent\venu\lib\site-packages` ，然后找到里面的 `\xadmin\plugins\importexport.py` 文件，修改如下

  ```python
  # 大约在 47-50 行之间
  from django.db import transaction
  
  # from import_export.admin import DEFAULT_FORMATS, SKIP_ADMIN_LOG, TMP_STORAGE_CLASS
  from import_export.admin import DEFAULT_FORMATS, ImportMixin, ImportExportMixinBase
  
  from import_export.resources import modelresource_factory
  ```

+ 如图所示

  ![](https://gitee.com/zxiaosi/image/raw/master/Project/Python/Django-StudentMS/报错.png)

+ 重启启动服务

  ```python
  python manage.py runserver
  ```

#### 5. 进入站点

+ 浏览器内输入

  >http://127.0.0.1:8000/xadmin/

+ 输入账号与密码

  ```python
  账号：admin
  密码：admin123
  ```

### 使用说明

####   1.**学生管理系统**

![DjangoStudent_1](https://gitee.com/zxiaosi/img/raw/master/Python/DjangoStudent_1.png)

####   2.学生信息的增操作

![DjangoStudent_2](https://gitee.com/zxiaosi/img/raw/master/Python/DjangoStudent_2.png)

####   3.学生信息的删操作

![DjangoStudent_3](https://gitee.com/zxiaosi/img/raw/master/Python/DjangoStudent_3.png)

####   4.学生信息的改操作

![DjangoStudent_4](https://gitee.com/zxiaosi/img/raw/master/Python/DjangoStudent_4.png)



### 其他

####  1.搜索(搜索内容可以是学生姓名、班级名、课程号)

![DjangoStudent_5](https://gitee.com/zxiaosi/img/raw/master/Python/DjangoStudent_5.png)

####   2.过滤器(按性别过滤)

![DjangoStudent_6](https://gitee.com/zxiaosi/img/raw/master/Python/DjangoStudent_6.png)

#### 3.主题

![DjangoStudent_7](https://gitee.com/zxiaosi/img/raw/master/Python/DjangoStudent_7.png)