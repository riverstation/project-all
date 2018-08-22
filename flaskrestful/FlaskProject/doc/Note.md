# Flask


## 第三方使用流程
- 安装插件
- 初始化插件
- 使用插件 


## Flask-Script
- 使Flask支持命令行参数
- 安装
    - pip install flask-script
    
    
## Flask-SQLAlchemy
- 安装
    - pip install flask-sqlalchemy
- 初始化
    - 使用App构建 SQLAlchemy
- 使用
    - 定义模型
        - 继承自  db.Model
        - 定义字段
            - 主键
    - 映射到数据库中
        - 直接使用的shell
        - 导入 db
            - 创建 table
            - db.create_all()
            - 删除 table
            - db.drop_all()
        - 坑点
            - 如果文件没有被导入
            - 这个文件就从来不会被加载
            - 我们的环境就不会知道你的文件存在
            

## Flask-Migrate
- 安装
    - pip install flask-migrate
- 初始化
    - 使用app和db进行初始化
    - 结合flask-script使用
        - manager.add_command("db", MigrateCommand)
- 使用
    - python manage.py db
    - init 初始化， 只调用一次
    - migrate 生成迁移文件
    - upgrade 执行迁移文件的升级，增量式操作
    - downgrade 执行迁移文件的降级
    - upgrade，downgrade 实际上都是迁移文件中的函数
- 如果文件没有被加载过，迁移文件是不知道文件的存在的，不能生成文件


## Flask-Caching
- 安装
    - pip install flask-caching
- 初始化
    - 使用app进行初始化
    - 还可以指定config
- 使用
    - xxx

    
### 单例
- 全局共享唯一实例
- 调用首先去缓存中获取
    - 不存在创建新实例进行返回
    - 存在直接返回实例
- 应用场景
    - 全局的工具类
    - 连接器
        - Redis客户端
        - MySQL客户端
        - 通信队列
        

### 环境
- 开发环境
- 测试环境
- 演示环境
    - 预上线
    - 产品使用
- 线上环境（生产环境）


### 项目跟随电脑自动切换环境
- 动态获取环境变量中的运行环境
- 环境根据预设进行匹配，加载对应环境
- 如果不存在环境变量，我们加载默认环境


### 开发工具
- 集成IDE
- 万能键   alt + enter


### 循环引用
- 如果所有的导报都直接导入
- 很有可能出现循环引用
    - A -> B
    - B -> C
    - C -> A
    
### 缓存
- 优化加载
- flask中缓存提供了两个实现
    - flask-cache   不适用于新版本
    - flask-caching   新版本旧版本都兼容
    
    
### 接口开发
- 实际上就是路由加函数的开发
- RESTful
    - 概念
    - 编写规则


### 开发接口
- 电影接口
- 确认需求
- 设计表结构
    - m_id
    - m_name
    - m_duration
- 设计接口
    -   API   /movies/
    - 请求参数
        - device   必须
- 编写接口


#### 编程
- 面向对象
- 面向过程
- 面向切面
- 面向接口
    - 只关注输入，输出
    
#### Flask四大内置对象
- request
- session
- g
- config


#### Flask中的调试工具
- 可以在页面中使用Debugger进行调试
- 根据输入调试器的PIN，可以在页面中动态调试程序


#### 优秀程序
- MTV   解耦和
- 高内聚
- 高内聚低耦合
    - 低耦合指的业务逻辑，视图展示是完全剥离开的
    - 高内聚值的，相同数据额操作，都在一块实现
    
#### HTML事件
- onready
    - 页面准备好了
- onload
    - 页面加载完成
- 准备好了指的是页面基础结构加载好了
- 加载完成，指图片等都加载完毕
- ready执行优于load

    

