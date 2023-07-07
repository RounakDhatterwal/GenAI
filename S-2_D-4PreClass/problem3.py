from pymongo import MongoClient

client = MongoClient('')
db = client['db']
collection = db['Customers']

cursor = collection.find()

for document in cursor:
    print(document)

client.close()