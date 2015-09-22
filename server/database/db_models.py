
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from app import app
from database import db

class Restaurant(db.Model):
    __tablename__="restaurants"
    restaurant_id = db.Column(Integer, primary_key=True)
    name = db.Column(db.String(100, unique=True))
    description = db.Column(db.String(255))
    logo_url = db.Column(db.Text)
    menu_items = relationship('MenuItem')

class MenuItem(db.Model):
    __tablename__="menuitems"
    menu_item_id = db.Column(Integer, primary_key=True)
    restaurant_id = Colum(Integer, ForeignKey('restaurant.restaurant_id'))
    description = db.Column(db.String(255))
    # Should this be JSON?
    images_urls = db.Column(db.Text)
