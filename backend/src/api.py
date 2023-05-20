import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
import sys

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

with app.app_context():
    db_drop_and_create_all()


# CORS Headers
@app.after_request
def after_request(response):
    response.headers.add(
        "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
    )
    response.headers.add(
        "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
    )
    return response


# get all available drinks with terse description
@app.route('/drinks', methods=['GET'])
def get_drinks():
    drinks = Drink.query.order_by(Drink.id).all()
    try:
        return jsonify({
            'success': True,
            'drinks': [drink.short() for drink in drinks]
        }), 200
    except BaseException:
        print(sys.exc_info())
        abort(500)


# get all available drinks in detail
@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(jwt):
    drinks = Drink.query.order_by(Drink.id).all()
    try:
        return jsonify({
            'success': True,
            'drinks': [drink.long() for drink in drinks]
        }), 200
    except BaseException:
        print(sys.exc_info())
        abort(500)


# create a drink
@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drink(jwt):
    body = request.get_json()
    title = body.get('title', None)
    recipe = body.get('recipe', None)

    # If any field is missed or recipe's type is not list, abort with 400.
    if (not title) or (not recipe):
        abort(400)
    try:
        # Drink constructor
        drink = Drink(title, json.dumps(recipe))
        drink.insert()

        return jsonify({
            'success': True,
            'drinks': drink.long()
        }), 200
    except BaseException:
        print(sys.exc_info())
        abort(500)


# update a drink
@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(jwt, drink_id):
    drink = Drink.query.filter(Drink.id == drink_id).one_or_none()
    if drink is None:
        abort(404)
    body = request.get_json()
    title = body.get('title', None)
    recipe = body.get('recipe', None)

    # If two fields are all missed, abort with 400.
    if (not title) and (not recipe):
        abort(400)

    # update recipe if the request contains recipe information
    # and assure that the type of recipe must be a list
    if recipe and (not isinstance(recipe, list)):
        abort(400)
    elif recipe and isinstance(recipe, list):
        drink.recipe = recipe if type(recipe) == str else json.dumps(recipe)

    # update title if the request contains title information
    if title:
        drink.title = title
    try:
        drink.update()
        return jsonify({
            'success': True,
            'drinks': [drink.long()]
        }), 200
    except BaseException:
        print(sys.exc_info())
        abort(500)


# delete a drink
@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(jwt, drink_id):
    drink = Drink.query.filter(Drink.id == drink_id).one_or_none()

    # If the drink does not exist, abort with 404
    if drink is None:
        abort(404)
    try:
        drink.delete()
        return jsonify({
            'success': True,
            'delete': drink_id
        }), 200
    except BaseException:
        print(sys.exc_info())
        abort(500)


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'success': False,
        'error': 400,
        'message': "Bad Request"
    }), 400


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 404,
        'message': "Resource Not Found"
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        'success': False,
        'error': 405,
        'message': "Method Not Allowed"
    }), 405


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        'success': False,
        'error': 422,
        'message': "Unprocessable Entity"
    }), 422


@app.errorhandler(500)
def unprocessable(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': "Internal Server Error"
    }), 500


@app.errorhandler(AuthError)
def handle_auth_error(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error
    }), error.status_code
