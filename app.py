from flask import Flask, session, g
import config
from exts import db, mail
from models import UserModel, EmailCaptchaModel
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate

app = Flask(__name__)

# 绑定配置文件
app.config.from_object(config)

# 初始化Flask-Migrate
migrate = Migrate(app, db)

# 通过这个调用，db被配置为与app一起工作，使用app的配置来连接数据库
db.init_app(app)

mail.init_app(app)

# 注册蓝图
app.register_blueprint(auth_bp)
app.register_blueprint(qa_bp)

# flask db init：只需执行一次
# flask db migrate：将orm模型生成迁移脚本
# flask db upgrade：将迁移脚本映射到数据库中

# 钩子函数(hook function): before_request / before_first_request / after_request 等

# @app.before_request 是 Flask 框架中的一个装饰器，它允许你注册一个在每次请求之前被调用的函数。这个函数会在 Flask 处理请求之前执行，可以用于执行一些预处理任务，比如验证用户身份、加载配置、记录日志等。
@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = UserModel.query.get(user_id)
        # Flask 的 g 对象是一个特殊的对象，它在每个请求中都是唯一的，并且用于存储请求期间的数据。这意味着每个请求都会有一个新的 g 对象，因此不会存在多个用户同时访问时覆盖的问题。
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)

# @app.context_processor 是 Flask 框架中的一个装饰器，它允许你为 Flask 应用的模板上下文（template context）添加全局变量或函数。当你在模板中渲染页面时，这些全局变量或函数将自动可用，无需在每个视图函数中显式地传递它们。
@app.context_processor
# 当你使用 @app.context_processor 装饰一个函数时，Flask 会自动调用这个函数，并将其返回值合并到模板的上下文中。这个函数通常返回一个字典，字典中的键值对将作为全局变量添加到模板中。
def my_context_processor():
    return {"user": g.user}

if __name__ == '__main__':
    app.run()

# 学习内容：
# url传参
# 邮件发送
# arm与数据库
# Jinja2模板
# cookie和session
# 搜索