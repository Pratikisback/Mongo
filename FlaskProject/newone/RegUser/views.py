

from newone.RegUser.controller import find_user, reg_user
from newone import api, Resource, make_response, app
from flask import Blueprint, request, jsonify

regblue = Blueprint('registerblue',__name__)
class Register(Resource):
    def post(self):

        data = request.get_json()

        username = data.get('username')
        password = data.get('password')
        if not username and not password:
            return make_response(jsonify({"message": 'User already exists'}), 200)
        existing_user = find_user(username)
        print(existing_user)
        if existing_user:
            return make_response(jsonify({"message": 'User already exists'}), 200)
        new_user = {"username": username, "password": password}
        result = reg_user(new_user)
        if result:
            return make_response(jsonify(
                {"Message": "User registered successfully", "userName": username, "userid": str(result.inserted_id)}))


class login(Resource):
    def post(self):


        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        userinfo = find_user(username)
        usernamedb = userinfo.get("username")
        passworddb = userinfo.get("password")

        if username == usernamedb and password == passworddb:
            return make_response(jsonify({"Message": "User logged in successfully"}))
        else:
            return make_response(jsonify({"Message": "Invalid Credentials"}))


api.add_resource(Register, '/register')
api.add_resource(login, '/login')



