
SECRET_KEY = "sadsa43284asda;hjmh"

# 数据库的配置信息
HOSTNAME = '172.23.23.68'
PORT = '3306'
DATABASE = 'zhiliaooa'
USERNAME = 'leoh'
PASSWORD = 'li123123'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


# vvlnwzfmgrpobbia
# 邮箱配置
MAIL_SERVER = 'smtp.QQ.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = '707568633@qq.com'
MAIL_PASSWORD = 'vvlnwzfmgrpobbia'
MAIL_DEFAULT_SENDER = '707568633@qq.com'