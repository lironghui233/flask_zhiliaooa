
SECRET_KEY = "sadsa43284asda;hjmh"

# 数据库的配置信息
HOSTNAME = ''
PORT = '3306'
DATABASE = 'zhiliaooa'
USERNAME = ''
PASSWORD = ''
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


# vvlnwzfmgrpobbia
# 邮箱配置
MAIL_SERVER = 'smtp.QQ.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_DEFAULT_SENDER = ''