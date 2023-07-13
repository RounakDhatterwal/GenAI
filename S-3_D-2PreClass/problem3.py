from pymongo import MongoClient

client = MongoClient()

db = client['db']

customers_collection = db['Customers']

result = customers_collection.find()

for document in result:
    print(document)

client.close()
