import random

users = [
    {"Name": "Aria Bakhtiar", "Staff ID": "AB20123"},
    {"Name": "Diya Eshwar", "Staff ID": "ES19672"},
    {"Name": "Marina Nash", "Staff ID": "MN23001"},
    {"Name": "Kain Leun", "Staff ID": "KL20984"},
    {"Name": "Sjaak Teunissen", "Staff ID": "ST25248"},
    {"Name": "me", "Staff ID": "1"}
]

items = [
    {"item no.": "1", "Name": "Tandoori chicken Pizza", "Price": "£13.00", "Description": "Tandoori Style sauce with veggies and chicken on pizza"},
    {"item no.": "2", "Name": "Chips", "Price": "£3.00", "Description": "Plain deep fried chips"},
    {"item no.": "3", "Name": "Side Salad", "Price": "£5.00", "Description": "Mixed veggies with balsamic vinegar sauce"},
    {"item no.": "4", "Name": "Still Water", "Price": "£1.00", "Description": "Mineral Water", "type": "drink"},
    {"item no.": "5", "Name": "Magherita", "Price": "£10.00", "Description": "tomato base with mozzarella"},
    {"item no.": "6", "Name": "Garlic Bread", "Price": "£4.00", "Description": "garlic butter on bread"},
    {"item no.": "7", "Name": "Mozzarella sticks", "Price": "£4.00", "Description": "pastry wrapped in mozzarella"},
    {"item no.": "8", "Name": "Lasagne", "Price": "£12.00", "Description": "layered between sheets of lasagne is minced beef,veggies and mozzarella"},
    {"item no.": "9", "Name": "Risotto", "Price": "£12.00", "Description": "Alboro rice, mushrooms and creamy sauce"},
    {"item no.": "10", "Name": "Lemonade", "Price": "£3.00", "Description": "sparkling lemon juice", "type": "drink"},
    {"item no.": "11", "Name": "Sparkling Water", "Price": "£2.00", "Description": "carbonated water", "type": "drink"}
]


def authenticate(users):
    while True:
        name = input("Enter Name: ")
        staff_id = input("Enter Staff ID: ")
        for user in users:
            if user["Name"] == name and user["Staff ID"] == staff_id:
                print(f"Welcome to our pizzeria! My name is {name}.")
                return True
        print("Name and ID do not match. Access denied.")


def table_number():
    while True:
        table_number = input("Enter table number: ")

        if table_number.isdigit():
            print("This is a whole number. Carry on to the next step")
            table = int(table_number)
            if 1 <= table <= 7:
                print("There's a table available")
                return table
            else:
                print("Table not found. Please put in a number between 1 and 7.")
        else:
            print("Error! Make sure the table is a number.")


def customers():
    while True:
        num = input("How many people are at the table? ")
        if num.isdigit():
            print("This is a whole number.")
            return int(num)
        else:
            print("Please enter whole numbers")


def show_menu():
    print("Our menu:")
    for item in items:
        print(item)


def take_orders(num_customers):
    orders = []
    drinks = [item for item in items if item.get("type") == "drink"]

    for customer in range(num_customers):
        customer_order = []
        print("Customer", customer + 1, "ordering")

        drink_ordered = False

        while True:
            order = input("Enter item number or type 'done': ").strip()

            if order.lower() == "done":
                break

            found = False
            for item in items:
                if item["item no."] == order:
                    customer_order.append(item)
                    found = True

                    if item.get("type") == "drink":
                        drink_ordered = True

                    break

            if not found:
                print("Item not found.")

        # Suggest drink if none ordered
        while not drink_ordered:
            random_drink = random.choice(drinks)
            print(f"Here's a random drink for you: {random_drink['Name']}")

            want_drink = input("Do you want this drink? (y/n): ").lower()

            if want_drink == "y":
                customer_order.append(random_drink)
                drink_ordered = True
            elif want_drink == "n":
                drink_ordered = True
            else:
                print("please write y or n")

        orders.append(customer_order)

    return orders


def print_receipt(orders):
    print("\n----- RECEIPT -----")

    total = 0
    customer_number = 1

    for customer_order in orders:
        print(f"\nCustomer {customer_number}:")

        for item in customer_order:
            print(f"{item['Name']} - {item['Price']}")

            price = float(item["Price"].replace("£", ""))
            total += price

        customer_number += 1

    print("\n-------------------")
    print(f"TOTAL: £{total:.2f}")  # 2 decimal places
    print("-------------------")


# main program
authenticate(users)
show_menu()
table = table_number()
num_customers = customers()
all_orders = take_orders(num_customers)
print_receipt(all_orders)


