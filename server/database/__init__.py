import constants
from app import app
from flask.ext import sqlalchemy

# Where should this go?
app.config['SQLALCHEMY_DATABASE_URI'] = constants.SQLALCHEMY_DATABASE_URI
db = sqlalchemy.SQLAlchemy()
