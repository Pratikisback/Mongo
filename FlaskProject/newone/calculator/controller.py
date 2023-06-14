from pymongo import MongoClient
from newone import client


def store_calculated_values(x,y, addval, mulval, subval, divval):
    result = client.Employees.calculated.insert_one({"FirstNumber": x, "SecondNumber": y, "Addval": addval, "Multipliedval": mulval, "SubtractedValue": subval, "Dividedvalue": divval})
    return result