dictionary = {}

def addSnack():
    id = input("Enter Snack Id ")
    if id in dictionary:
        print("Id Already available. \n")
        return 
    name = input("Enter Snack Name ")
    while True:
        try:
            price = float(input("Enter Snack Price "))
            break
        except ValueError:
            print("Please Enter Valid price")
    Snack  = {'name':name, 'price':price, 'availabilty':'y'}
    dictionary[id] = Snack
    print(f"Snack With {id} Added Sucessfully.\n")


def removeSnack():
    id = input("Enter Snack Id ")  
    if id not in dictionary:
        print("Please Enter Valid Id. \n")
    else :
        del dictionary[id]
        print(f"Stack with Id {id} removed Sucessfully.")


def updateSnack():
    id = input("Enter Snack Id ")
    if id in dictionary:
        print("Id Already available. \n")
        return 
    name = input("Enter Snack Name ")
    while True:
        try:
            price = float(input("Enter Snack Price "))
            break
        except ValueError:
            print("Please Enter Valid price")
    Snack  = {'name':name, 'price':price, 'quantity':10}
    dictionary[id] = Snack
    print(f"Snack With {id} Updated Sucessfully.\n") 


def record():
    id = input("Enter Snack Id you want to purchase ")
    if id in dictionary and dictionary[id]['availabilty'] == 'y':
        dictionary[id]['availabilty'] = 'n'
        print(f"Snack Sold is {dictionary[id]['name']}")
    else:
        print("Snack Out of stock \n")


def main():
    while True:
        print("1. Add Snack")
        print("2. Remove Snack")
        print("3. Update Snack")
        print("4. Record Snack")
        print("5. Exit")

        choice = input('Enter Your Choice ')

        if choice == '1':
            addSnack()
        elif choice == '2':
            removeSnack()
        elif choice == '3':
            updateSnack()
        elif choice == '4':
            record()
        elif choice == 5:
            break
        else:
            print("Please Enter Correct option")


main()

