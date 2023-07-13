from pymongo import MongoClient

client = MongoClient()

db = client['db']

customers_collection = db['Customers']

customers_collection.create_index('id', unique=True)

client.close()
