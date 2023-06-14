from flask import Flask, make_response
from flask_restful import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://localhost:27017/Employees")



class Calculator:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y
    def div(self, x, y):
        return x / y

    def mul(self, x, y):
        return x * y

