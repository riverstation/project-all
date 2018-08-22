# Django


## MySQL驱动
- mysqlclient
    - python2
    - python3 
    - 都能完美运行
    - 对mysql的安装，配置有要求
- mysql-python
    - python2 不错
    - python3 装不上
- pymysql
    - 综合战斗力最高的
    - python2
    - python3
    - 伪装 mysqlclient


### Django内置的权限和权限组
- 用户表
- 权限表
- 用户权限表
    - 用户和权限的多对多的关系

- 组表
- 组权限表
    - 权限和组的多对多关系
    
- 用户组表
    - 用户和组的多对多关系


### 迁移原理
- 分两部
    - 生成迁移文件
    - 执行迁移文件
- 生成迁移文件
    - 根据models
    - 根据以往迁移记录生成
- 执行迁移文件
    - 根据迁移记录来实现
        - 根据迁移文件的所属和应用来进行查询
        - 如果迁移记录存在，则不再执行
        - 不存在，执行，成功之后，记录迁移记录，失败不记录
        
        
### 开发的时候
- 都是从数据开始的
- 从模型开始
    - 由模型生成数据库表（小应用，普通开发）
    - 应用比较大，实际上需要先将表定义下来的，使用逆向生成models
        - 变更的就是元信息中 添加了一个 manage=False
        
### Views
- FBC
    - function based view
- CBV
    - class bases view

#### CBV
- 使用
    - 继承View
    - 注册路由使用  XXXView.as_view()
- 原理
    - as_view()最终还是返回返回
    - 判断
        - 关键字参数的key不能使用请求方法
        - 关键字参数的key必须是已经存在的属性
    - 定义View
        - 记录请求，参数
        - 通过dispatch进行分发
            - 根据请求方法进行分发
            - 请求方法小写
            - 和对应的方法名字的函数去对应
            - django支持的请求方法
            - HttpResponse子类

#### TemplateView
- 由三块组成
- 三个父类
    - TemplateResponseMixin
        - 渲染模板
    - ContextMixin
        - 获取上下文数据
    - View
        - 分发请求

#### ListView
- MultipleObjectTemplateResponseMixin
    - TemplateResponseMixin
    - get_template_names 重写
- BaseListView
    - View
    - MultipleObjectMixin
        - get
        - 渲染成response
        - ContextMixin
        - 还扩展了大量方法
            - QuerySet
            - Paginator


#### CSRF
- 防跨站攻击
- 使用中间件实现
    - process_view
    - 验证 POST中的csrfmiddlewaretoken
- 想通过CSRF
    - 禁用插件
    - 使用{% csrf_token %}
    - 使用隐藏标签输入
    - 装饰器豁免  csrf_exempt