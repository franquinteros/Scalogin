class Config:
    SECRET_KEY = ('B432dmkF390%*Ss129fn3?&!')

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'Root'
    MYSQL_PASSWORD = 'adminadmin'
    MYSQL_DB = 'Scalogin'    
    
config = {
    'development' : DevelopmentConfig
}