class Config:
    SECRET_KEY = ('B432dmkF390%*Ss129fn3?&!')

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'adminadmin'
    MYSQL_DB = 'Scalogin'    
    
config = {
    'development' : DevelopmentConfig
}