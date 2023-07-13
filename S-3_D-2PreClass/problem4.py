from pymongo import MongoClient

# Connect to the MongoDB server (assumes running locally on default port)
client = MongoClient()

db = client['db']

customers_collection = db['Customers']

projection = {
    'id': 3, 
    'name': 'Rama',
    'email': 'rama@gmail.com'
}

result = customers_collection.find({}, projection)

for document in result:
    print(document)

client.close()
