import csv


class Zomato:
    def __init__(self):
        self.menu = []
        self.orders = []
        self.order_id_counter = 1

    def load_menu(self, menu_file):
        with open(menu_file, 'r') as file:
            reader = csv.DictReader(file)
            self.menu = list(reader)

    def save_menu(self, menu_file):
        with open(menu_file, 'w', newline='') as file:
            fieldnames = ['dish_id', 'dish_name', 'price', 'availability']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.menu)

    def display_menu(self):
        print("Menu:")
        print("-----")
        for dish in self.menu:
            print(f"Dish ID: {dish['dish_id']}")
            print(f"Dish Name: {dish['dish_name']}")
            print(f"Price: {dish['price']}")
            print(f"Availability: {dish['availability']}")
            print("-----")

    def add_dish(self, dish_id, dish_name, price):
        self.menu.append({
            'dish_id': dish_id,
            'dish_name': dish_name,
            'price': price,
            'availability': 'yes'
        })
        print(f"Added dish with ID {dish_id} to the menu.")

    def remove_dish(self, dish_id):
        for dish in self.menu:
            if dish['dish_id'] == dish_id:
                self.menu.remove(dish)
                print(f"Removed dish with ID {dish_id} from the menu.")
                return
        print(f"No dish found with ID {dish_id}.")

    def update_availability(self, dish_id, availability):
        for dish in self.menu:
            if dish['dish_id'] == dish_id:
                dish['availability'] = availability
                print(f"Updated availability of dish with ID {dish_id} to {availability}.")
                return
        print(f"No dish found with ID {dish_id}.")

    def take_order(self, customer_name, dish_ids):
        order_dishes = []
        for dish_id in dish_ids:
            found = False
            for dish in self.menu:
                if dish['dish_id'] == dish_id:
                    if dish['availability'] == 'yes':
                        order_dishes.append(dish)
                        found = True
                    else:
                        print(f"Dish with ID {dish_id} is not available.")
                        break
            if not found:
                print(f"No dish found with ID {dish_id}.")
                break
        else:
            order_id = self.order_id_counter
            self.order_id_counter += 1
            order = {
                'order_id': order_id,
                'customer_name': customer_name,
                'dishes': order_dishes,
                'status': 'received'
            }
            self.orders.append(order)
            print(f"Order {order_id} received for customer {customer_name}.")

    def update_order_status(self, order_id, status):
        for order in self.orders:
            if order['order_id'] == order_id:
                order['status'] = status
                print(f"Updated status of order {order_id} to {status}.")
                return
        print(f"No order found with ID {order_id}.")

    def review_orders(self):
        print("All Orders:")
        print("------------")
        for order in self.orders:
            print(f"Order ID: {order['order_id']}")
            print(f"Customer Name: {order['customer_name']}")
            print("Dishes:")
            for dish in order['dishes']:
                print(f"- {dish['dish_name']} ({dish['dish_id']})")
            print(f"Status: {order['status']}")
            print("------------")

    def run(self):
        self.load_menu('Sprint_1_Day_4\\PreClass\\menu.csv')
        while True:
            print("\nZesty Zomato - Main Menu")
            print("------------------------")
            print("1. Display Menu")
            print("2. Add Dish")
            print("3. Remove Dish")
            print("4. Update Availability")
            print("5. Take Order")
            print("6. Update Order Status")
            print("7. Review Orders")
            print("8. Save and Exit")

            choice = input("Enter your choice (1-8): ")
            print()

            if choice == '1':
                self.display_menu()
            elif choice == '2':
                dish_id = input("Enter dish ID: ")
                dish_name = input("Enter dish name: ")
                price = input("Enter price: ")
                self.add_dish(dish_id, dish_name, price)
            elif choice == '3':
                dish_id = input("Enter dish ID to remove: ")
                self.remove_dish(dish_id)
            elif choice == '4':
                dish_id = input("Enter dish ID to update availability: ")
                availability = input("Enter availability (yes/no): ")
                self.update_availability(dish_id, availability)
            elif choice == '5':
                customer_name = input("Enter customer name: ")
                dish_ids = input("Enter dish IDs (comma-separated): ").split(',')
                self.take_order(customer_name, dish_ids)
            elif choice == '6':
                order_id = input("Enter order ID to update status: ")
                status = input("Enter new status: ")
                self.update_order_status(order_id, status)
            elif choice == '7':
                self.review_orders()
            elif choice == '8':
                self.save_menu('menu.csv')
                break
            else:
                print("Invalid choice. Please try again.")


zomato = Zomato()
zomato.run()
