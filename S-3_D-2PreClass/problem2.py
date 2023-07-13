from pymongo import MongoClient

client = MongoClient()

db = client['db']

customers_collection = db['Customers']

customers_data = [
    {
        'id': 1,
        'name': 'Ram',
        'email': 'ram@gmail.com',
        'address': 'India',
        'phone_number': '12334567'
    },
    {
        'id': 2,
        'name': 'Sam',
        'email': 'sam@gmail.com',
        'address': 'Pune',
        'phone_number': '4342532'
    }
]
customers_collection.insert_many(customers_data)

client.close()
