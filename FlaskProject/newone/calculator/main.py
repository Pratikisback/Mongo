from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client['Employees']
collection = db['Users']
#
#
# b = {"Name": "Pratik", "Age": 20}
#
# a = collection.insert_one(b)
# print(b)
username = "Poreto"
result = collection.find_one({"username": username})
print(result)