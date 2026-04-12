# Assignment-2-Sem-B







import random
def authenticate(users):
    # Keep asking for a correct name
    
    while True:
        name = input("Enter Name: ")
        # Keep asking for a correct staff ID
        staff_id = input("Enter Staff ID: ")
        for user in users:
            if user["Name"] == name and user["Staff ID"] == staff_id:
                print(f"Welcome to our pizzeria! My name is {name}.") 
                return False
            

        print("Name and ID do not match. Access denied.")

servers = [
    {"Name": "Aria Bakhtiar", "Staff ID": "AB20123"},
    {"Name": "Diya Eshwar", "Staff ID": "ES19672"},
    {"Name": "Marina Nash", "Staff ID": "MN23001"},
    {"Name": "Kain Leun", "Staff ID": "KL20984"},
    {"Name": "Sjaak Teunissen", "Staff ID": "ST25248"}
]
#authenticate(servers)

# Table number function

def table_number():
    table = 0 
    while True:
        table_number = input("Enter table number: ")

        if table_number.isdigit():
            print("This is a whole number. Carry on to the next step")
            if int(table_number):
                table = int(table_number)+ table
                if table >= 1 and table <= 7:
                    print("There's a table available")
                    return False
                else:
                    print("Table not found. Please put in a number between 1 and 7.")
            else:
                print("Make sure the table number is a whole number") 
        else:
            print("Error! Make sure the table is a number.")

def customers():
    while True:
        customers = input("How many people are at the table? ")
        if customers.isdigit():
            print("This is a whole number.")
            return False
        else:
            print("Please enter whole numbers")
                
    print(f"{customers} customers at the table.")
    
#table_number()
#customers()

items = [
    {"Name": "Tandoori chicken Pizza", "Price": "£13.00", "Description": "Tandoori Style sauce with veggies and chicken on pizza"},
    {"Name": "Chips", "Price": "£3.00","Description": "Plain deep fried chips"},
    {"Name": "Side Salad", "Price": "£5.00","Description": "Mixed veggies with balsamic vinegar sauce"},
    {"Name": "Still Water", "Price": "£1.00","Description": "Mineral Water"},
    {"Name": "Magherita", "Price": "£10.00","Description": "tomato base with mozzarella"},
    {"Name": "Garlic Bread", "Price": "£4.00","Description": "garlic butter on bread"},
    {"Name": "Mozzarella sticks", "Price": "£4.00","Description": "pastry wrapped in mozzarella"},
    {"Name": "Lasagne", "Price": "£12.00","Description": "layered between sheets of lasagne is minced beef,veggies and mozzarella"},
    {"Name": "Risotto", "Price": "£12.00","Description": "Alboro rice, mushrooms and creamy sauce"},
    {"Name": "Lemonade", "Price": "£3.00","Description": "sparkling lemon juice"},
    {"Name": "Sparkling Water", "Price": "£2.00","Description": "carbonated water"}
]


#menu function
def show_menu():
    print("Our menu:")
    for item in items:
        print(f"{item['Name']} : {item['Price']} : {item['Description']}")


def choice():
    while True:
        order = input("what would you like to eat")
        for food in items:
            if food["Name"] == order:
                answer=input("do you want add more? If yes put Y and no put N:")
                user_input = input("Enter your choice: ")

                if user_input == "y":
                  print("What would you like to order?\n")
                elif user_input == "n":
                  print("Next Order")
                  return False 
            for item in items:
                if item["Name"] == order:
                     print("This is on the menu!")
                     append(order)
                     return True
            else:
                print("Please use the menu provided, this is not on the menu")
#take order function
def take_orders():
    order_1 = []
    order_2 = []
    order_3 = []
    order_4 = []
    num_people = input("How many people are ordering today.There are 4 available spaces, how many are ordering today?: ")
    if num_people == "1":
        print("1")
        choice(order_1)
    elif num_people == "2":
        choice(order_2)
    elif num_people == "3":
        choice(order_3)
    elif num_people == "4":
        choice({"1": order_1, "2": order_2, "3": order_3, "4": order_4}.get(num_people, []))
        print(order_1)
        print(order_2)
        print(order_3)
        print(order_4)
        
def drinks():
    drinks = ["Carbonated water ", "Still water", "Lemonade"]
    drink = input("would you like a drink, enter y or n")
    if drink == "y":
        print("Please select a drink: ")
    elif drink == "n":
        print(random.choice(drinks ))
show_menu()
take_orders()
drinks()
#all_orders = take_orders()
