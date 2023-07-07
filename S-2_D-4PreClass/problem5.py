from pymongo import MongoClient


client = MongoClient('')
db = client['db']
collection = db['Customers']

filter = {'id': '3'}

customer = collection.find_one(filter)

print(customer)

client.close()