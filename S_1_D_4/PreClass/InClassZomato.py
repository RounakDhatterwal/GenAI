import json

# Global Variables
menu = []      # List to store the menu items
orders = []    # List to store the orders
menu_file = "menu.json"      # File to store the menu data
orders_file = "orders.json"  # File to store the order data

# Function to save the menu data to a JSON file
def save_menu():
    with open(menu_file, 'w') as file:
        json.dump(menu, file)

# Function to save the order data to a JSON file
def save_orders():
    with open(orders_file, 'w') as file:
        json.dump(orders, file)

# Function to load the menu data from a JSON file
def load_menu():
    try:
        with open(menu_file, 'r') as file:
            menu.extend(json.load(file))
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty menu
        menu.clear()

# Function to load the order data from a JSON file
def load_orders():
    try:
        with open(orders_file, 'r') as file:
            orders.extend(json.load(file))
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty list of orders
        orders.clear()

# Function to display the menu
def display_menu():
    for dish in menu:
        print(f"Dish ID: {dish['dish_id']}")
        print(f"Dish Name: {dish['dish_name']}")
        print(f"Price: {dish['price']}")
        print(f"Availability: {dish['availability']}")
        print()

# Function to add a new dish to the menu
def add_dish():
    dish_id = input("Enter dish ID: ")
    dish_name = input("Enter dish name: ")
    price = input("Enter price: ")
    availability = input("Enter availability (yes/no): ")
    dish = {
        'dish_id': dish_id,
        'dish_name': dish_name,
        'price': price,
        'availability': availability
    }
    menu.append(dish)
    save_menu()

# Function to remove a dish from the menu
def remove_dish():
    dish_id = input("Enter dish ID to remove: ")
    for dish in menu:
        if dish['dish_id'] == dish_id:
            menu.remove(dish)
            save_menu()
            print("Dish removed successfully.")
            break
    else:
        print("Dish not found.")

# Function to update the availability of a dish
def update_dish_availability():
    dish_id = input("Enter dish ID to update availability: ")
    availability = input("Enter new availability (yes/no): ")
    for dish in menu:
        if dish['dish_id'] == dish_id:
            dish['availability'] = availability
            save_menu()
            print("Availability updated successfully.")
            break
    else:
        print("Dish not found.")

# Function to take a new order
def take_order():
    customer_name = input("Enter customer name: ")
    dish_ids = input("Enter dish IDs (comma-separated): ").split(",")
    order = {
        'order_id': len(orders) + 1,
        'customer_name': customer_name,
        'dish_ids': dish_ids,
        'status': 'received'
    }
    orders.append(order)
    save_orders()

# Function to update the status of an order
def update_order_status():
    order_id = input("Enter order ID to update status: ")

def update_order_status():
    order_id = input("Enter order ID to update status: ")
    status = input("Enter new status: ")
    for order in orders:
        if order['order_id'] == int(order_id):
            order['status'] = status
            save_orders()
            print("Status updated successfully.")
            break
    else:
        print("Order not found.")

# Function to review all the orders
def review_orders():
    for order in orders:
        print(f"Order ID: {order['order_id']}")
        print(f"Customer Name: {order['customer_name']}")
        print(f"Dish IDs: {order['dish_ids']}")
        print(f"Status: {order['status']}")
        print()

# Function to exit the program
def exit_program():
    save_menu()
    save_orders()
    print("Exiting the program...")

# Main program loop
if __name__ == "__main__":
    load_menu()
    load_orders()

    while True:
        # Display menu options to the user
        print("\nZesty Zomato - Main Menu")
        print("1. Display Menu")
        print("2. Add Dish")
        print("3. Remove Dish")
        print("4. Update Dish Availability")
        print("5. Take Order")
        print("6. Update Order Status")
        print("7. Review Orders")
        print("8. Exit")

        # Get user input for menu choice
        choice = input("Enter your choice (1-8): ")

        # Perform the corresponding action based on user input
        if choice == "1":
            display_menu()
        elif choice == "2":
            add_dish()
        elif choice == "3":
            remove_dish()
        elif choice == "4":
            update_dish_availability()
        elif choice == "5":
            take_order()
        elif choice == "6":
            update_order_status()
        elif choice == "7":
            review_orders()
        elif choice == "8":
            exit_program()
            break
        else:
            print("Invalid choice. Please try again.")
