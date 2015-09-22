import flask
from flask import abort
from flask import json
from flask import make_response
from flask import request
from flask import url_for
from flask.ext.sqlalchemy import SQLAlchemy

from app import app
import constants
from database import db

#Temporary
import fake_data as f

@app.route('/api/v1.0/restaurants', methods=['GET'])
def get_restaurants():
    # Request restaurants from database

    restaurants = f.restaurants
    return json.jsonify({
        'restaurants': [return_public_restaurant(restaurant) for restaurant in restaurants]
    })

# Need to add authentication for admin account
@app.route('/api/v1.0/restaurants', methods=['POST'])
def create_restaurant():
    if not request.json or not 'name' in request.json:
        abort(404)

    # Insert restaurant to db
    
    # This is just a temporary hack. Need to create a service call to controller that inserts to DB
    restaurants = f.restaurants
    restaurant = {
        'id': restaurants[-1]['id'] + 1,
        'name': request.json['name'],
        'description': request.json.get('description', "")
    }
    restaurants.append(restaurant)
 
    return json.jsonify({
        'restaurant': return_public_restaurant(restaurant)
    }), 201

@app.route('/api/v1.0/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):

    # Request restaurant from database, replace this hack
    restaurants = f.restaurants
    restaurant = [restaurant for restaurant in restaurants if restaurant['id'] == restaurant_id]
    if len(restaurant) == 0:
        abort(404)
    return json.jsonify({
        'restaurant': return_public_restaurant(restaurant[0])
    })

@app.route('/api/v1.0/restaurants/<int:restaurant_id>', methods=['PUT'])
def update_restaurant(restaurant_id):

    # Update restaurant from database
    restaurants = f.restaurants
    restaurant = [restaurant for restaurant in restaurants if restaurant['id'] == restaurant_id]
    if len(restaurant) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    restaurant[0]['name'] = request.json.get('name', restaurant[0]['name'])
    restaurant[0]['description'] = request.json.get('description', restaurant[0]['description'])
    return json.jsonify({
        'restaurant': return_public_restaurant(restaurant[0])
    })

@app.route('/api/v1.0/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):

    # Delete restaurant from database
    restaurants = f.restaurants
    restaurant = [restaurant for restaurant in restaurants if restaurant['id'] == restaurant_id]
    if len(restaurant) == 0:
        abort(404)
    restaurants.remove(restaurant[0])
    return json.jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(json.jsonify({'error': 'Not found'}), 404)

def return_public_restaurant(restaurant):
    public_restaurant = {}
    for field in restaurant:
        if field == 'id':
            public_restaurant['uri'] = url_for('get_restaurant', restaurant_id=restaurant['id'], _external=True)
        else:
            public_restaurant[field] = restaurant[field]
    return public_restaurant

# This is just for debug mode so you don't have to run Apache
if __name__ == '__main__':
    app.debug = True
    app.run()

