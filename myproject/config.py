import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"

        #db = {
         #       'user' : 'flask',
          #      'password' :'tnektnek12',
           #     'host' : '127.0.0.1',
            #    'port' : '3306',
             #   'database' : 'blogger'
#}
#QLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"