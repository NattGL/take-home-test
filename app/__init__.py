import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

BASEDIR = os.path.normpath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASEDIR, '.env'))

app = Flask(__name__)
CORS(app)
conf = os.environ.get('FLASK_ENV', 'config.BaseConfig')
app.config.from_object(conf)

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

name_swagger_api = Api(app,
                       catch_all_404s=True,
                       version='1.0',
                       title='Swagger dataset handler',
                       description='Swagger Rest API dataset handler')
api = name_swagger_api.namespace('api/v1', description='All operations')

from . import views
from . import models
from . import swagger
from . import services
