from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for menu and orders
menu = [
    {"id": 1, "name": "Margherita Pizza", "price": 12.99, "availability": True},
    {"id": 2, "name": "Spaghetti Carbonara", "price": 10.99, "availability": True},
    {"id": 3, "name": "Chicken Biryani", "price": 9.99, "availability": False},
    # Add more dishes here...
]

orders = []


# Home page - Show menu
@app.route('/')
def index():
    return render_template('zomato.html', menu=menu)


# Add a new dish to the menu
@app.route('/add_dish', methods=['GET', 'POST'])
def add_dish():
    if request.method == 'POST':
        dish_id = int(request.form['dish_id'])
        dish_name = request.form['dish_name']
        dish_price = float(request.form['dish_price'])
        dish_availability = True if request.form.get('dish_availability') else False

        menu.append({"id": dish_id, "name": dish_name, "price": dish_price, "availability": dish_availability})
        return redirect(url_for('index'))

    return render_template('addDish.html')


# Remove a dish from the menu
@app.route('/remove_dish/<int:dish_id>')
def remove_dish(dish_id):
    global menu
    menu = [dish for dish in menu if dish['id'] != dish_id]
    return redirect(url_for('index'))


# Update the availability of a dish
@app.route('/update_availability/<int:dish_id>/<string:availability>')
def update_availability(dish_id, availability):
    dish = next((dish for dish in menu if dish['id'] == dish_id), None)
    if dish:
        dish['availability'] = (availability == 'True')
    return redirect(url_for('index'))


# Take a new order
@app.route('/new_order', methods=['GET', 'POST'])
def new_order():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        dish_ids = request.form.getlist('dish_ids')

        # Check if all dishes are available
        available_dishes = [dish for dish in menu if dish['id'] in map(int, dish_ids)]
        if len(available_dishes) != len(dish_ids):
            return "Some of the selected dishes are not available!"

        # Generate a unique order ID
        order_id = len(orders) + 1

        # Create the order and add it to the list
        order = {"id": order_id, "customer_name": customer_name, "dish_ids": dish_ids, "status": "received"}
        orders.append(order)

        return redirect(url_for('view_orders'))

    return render_template('newOrder.html', menu=menu)


# Update the status of an order
@app.route('/update_order_status/<int:order_id>/<string:status>')
def update_order_status(order_id, status):
    order = next((order for order in orders if order['id'] == order_id), None)
    if order:
        order['status'] = status
    return redirect(url_for('view_orders'))


# View all orders
@app.route('/view_orders')
def view_orders():
    return render_template('viewOrders.html', orders=orders)


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
