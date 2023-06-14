from newone import Resource,api,app, Flask, Calculator,  make_response
from newone.calculator.controller import  store_calculated_values
from flask import Blueprint, request, jsonify


calblue = Blueprint('Calculatorblue',__name__)

class calculate1(Resource):
    def post(self):
        dataa = request.get_json()
        num1  = dataa.get('first no')
        num2  = dataa.get('second no')
        calobj = Calculator()
        mulval = calobj.mul(num1, num2)
        addval = calobj.add(num1, num2)
        subval = calobj.sub(num1, num2)
        divval = calobj.div(num1, num2)
        res = store_calculated_values(num1, num2, mulval, addval, subval, divval)
        if res:
            return make_response(jsonify({
                "FirstNumber" : num1,
                "SecondNumber" : num2,
                "AddedResult": addval,
                "MultipiedResult": mulval,
                "subtractedValue": subval,
                "DividedResult" : divval

            }))

api.add_resource(calculate1, '/calculate')
