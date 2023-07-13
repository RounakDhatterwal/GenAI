from pymongo import MongoClient

client = MongoClient()

db = client['db']

customers_collection = db['Customers']

customer = customers_collection.find_one({'id': 3})

print(customer)

client.close()
