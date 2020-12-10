# Django-Student

### 介绍
  Django 实现学生后台管理系统

### 软件架构
  Python3.7+Django2.2+Xadmin2 实现学生后台管理系统


### 安装教程
####   1.配置Python3.6(及以上)的虚拟环境

####   2.装包

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

####   3.启动服务

+ 进入“终端”CMD命令，进入项目apps文件夹

  ```python
  cd apps
  ```

+ 启动服务

  ```python
  python manage.py runserver
  ```


#### 4.进入站点

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