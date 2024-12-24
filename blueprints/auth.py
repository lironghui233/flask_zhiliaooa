from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from pyexpat.errors import messages

from exts import mail,db
from flask_mail import Message
import string
import random

from models import EmailCaptchaModel
from .forms import RegisterForm, LoginForm
from models import UserModel
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("auth", __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        # 格式验证
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            # 数据库验证
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱再数据库中不存在！")
                return redirect(url_for('auth.login'))
            if check_password_hash(user.password, password):
                # cookie:
                # cookie中不适合存错太多的数据，只适合存储少量的数据
                # cookie一般用来存放登陆授权的东西
                # flask中的session，是经过加密后存储在cookie中的
                session['user_id'] = user.id
                # 跳转到首页
                return redirect("/")
            else:
                print("密码错误！")
                return redirect(url_for('auth.login'))
        else:
            print(form.errors)
            return redirect(url_for('auth.login'))



@bp.route('/logout')
def logout():
    session.clear()
    return redirect("/")

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        # 表单验证：flask-wtf: wtforms
        # 格式验证
        form = RegisterForm(request.form)
        if form.validate():
            # 注册
            email = form.email.data
            username = form.username.data
            password = form.password.data
            # 密码存储进数据库需要加密（隐私保护）
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            # 跳转到登录页
            return redirect(url_for('auth.login'))
        else:
            print(form.errors)
            # 重新跳转回注册页面 注册
            return redirect(url_for('auth.register'))

# bp.route：如果没有指定methods参数，默认就是GET请求
@bp.route('/captcha/email')
def get_captcha_email():
    email = request.args.get("email")
    # 随机4位数字验证码
    source = string.digits*4
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)
    # 发送邮件
    message = Message(subject="知了验证码", recipients=[email], body=f"您的验证码是{captcha}")
    mail.send(message)
    # 缓存验证码： memcached/redis
    # 代替方案，存mysql
    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    # RESTful API:  {code: 200/400/500, message: "", data: {}}
    return jsonify({"code":200, "message":"ok", "data": None})

@bp.route('/mail/test')
def mail_test():
    message = Message(subject="test", recipients=["1310528969@qq.com"], body="这是一条测试邮件")
    mail.send(message)
    return "邮件发送成功！"