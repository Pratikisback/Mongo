from flask_restful import Resource, Api
from flask import Flask, request, make_response, jsonify
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)


