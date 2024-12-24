# 知了问答平台

这是一个基于 Flask 的问答平台系统，采用传统的前后端不分离架构设计。用户可以注册、登录、发布问题、回答问题，支持问题搜索等功能。

## 技术架构

### 后端技术栈

- Flask：Web框架
- Flask-SQLAlchemy：ORM框架
- Flask-Mail：邮件发送
- Flask-Migrate：数据库迁移
- PyMySQL：MySQL数据库驱动
- WTForms：表单验证

### 前端技术栈

- Bootstrap 4.6：UI框架
- jQuery 3.6：JavaScript库
- Jinja2：模板引擎

### 数据库

- MySQL：主数据库
- 字符集：utf8mb4

## 核心模块

### 1. 用户认证模块 (auth)

- 用户注册
- 邮箱验证码
- 用户登录
- 会话管理
- 登出功能

### 2. 问答模块 (qa)

- 问题管理
- 回答管理
- 问题列表
- 问题详情
- 问题搜索

### 3. 数据模型 (models)

- UserModel：用户模型
- EmailCaptchaModel：邮箱验证码模型
- QuestionModel：问题模型
- AnswerModel：回答模型

### 4. 表单验证 (forms)

- RegisterForm：注册表单验证
- LoginForm：登录表单验证
- QuestionForm：问题表单验证
- AnswerForm：回答问题单验证

## 技术要点

### 1. 用户认证

- 基于 Session 的用户认证
- 密码加密存储
- 邮箱验证码注册
- 登录状态维护
- 装饰器实现登录验证

### 2. 数据库设计

- ORM模型关系映射
- 外键关联
- 一对多关系处理
- 数据库迁移管理

### 3. 安全特性

- CSRF 防护
- 密码加密存储
- 表单验证
- 会话管理

### 4. 前端交互

- AJAX异步请求
- 表单验证
- 响应式布局
- 用户友好提示

## 功能特性

### 用户功能

- [X] 用户注册
- [X] 邮箱验证
- [X] 用户登录
- [X] 用户登出
- [X] 登录状态维护

### 问答功能

- [X] 发布问题
- [X] 问题列表展示
- [X] 问题详情查看
- [X] 发表回答
- [X] 问题搜索
- [X] 按时间排序

### 其他功能

- [X] 邮件发送
- [X] 验证码生成
- [X] 全局用户状态
- [X] 响应式布局

## 项目结构

flask_zhiliaooa/

├── app.py # 应用入口

├── config.py # 配置文件

├── exts.py # 扩展文件

├── models.py # 数据模型

├── decorators.py # 装饰器

├── blueprints/ # 蓝图目录

│ ├── auth.py # 认证蓝图

│ ├── qa.py # 问答蓝图

│ └── forms.py # 表单验证

├── templates/ # 模板文件

└── static/ # 静态文件

## 环境要求

- Python 3.7+
- MySQL 5.7+
- 支持现代浏览器

## 安装部署

1. 克隆项目

   ```
   git clone [项目地址]
   ```
2. 安装依赖

   ```
   pip install -r requirements.txt
   ```
3. 配置数据库

   ```
   config.py
   HOSTNAME = 'localhost'
   PORT = '3306'
   DATABASE = 'zhiliaooa'
   USERNAME = 'your_username'
   PASSWORD = 'your_password'
   ```
4. 初始化数据库

   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```
   1. 运行项目

      ```
      flask run
      ```
      ## 项目所需的主要依赖包


      1. 核心框架：

         * Flask - Web框架
         * Jinja2 - 模板引擎
      2. 数据库相关：

         * Flask-SQLAlchemy - ORM框架
         * PyMySQL - MySQL驱动
         * Flask-Migrate - 数据库迁移工具
      3. 表单和验证：

         * WTForms - 表单验证
         * email-validator - 邮箱验证
      4. 邮件功能：

         * Flask-Mail - 邮件发送
      5. 安全相关：

         * Werkzeug - 提供密码哈希等安全功能
      6. 开发工具：

         * python-dotenv - 环境变量管理

      ## 开发计划

      ### 待实现功能

      - [ ] 用户头像上传
      - [ ] 富文本编辑器
      - [ ] 评论点赞功能
      - [ ] 问题标签功能
      - [ ] 用户个人中心

      ## 贡献指南

      欢迎提交 Issue 和 Pull Request。在提交代码前，请确保：

      1. 代码符合项目规范
      2. 添加必要的注释
      3. 更新相关文档

      ## 许可证

      本项目采用 MIT 许可证
