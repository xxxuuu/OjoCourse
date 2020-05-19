COURSE_CONFIG = {
    'host': '',
    'auth': ('', ''),
    'protocol': 'http',
}

COURSE_UPDATE_INTERVAL = 3600

DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = ''
DB_DATABASE = ''
DB_CHARSET = 'utf8mb4'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%d/%s?charset=%s' % (
    DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE, DB_CHARSET
)
