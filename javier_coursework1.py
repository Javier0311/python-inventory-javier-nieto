# Messages
welcoming = "Welcome to the Inventory Management System"
mainMenu = "1. Add Item \n 2. View Inventory \n 3. Update Item \n 4. Remove Item \n 5. Exit"
navType=0

# Dictionary to Inventory
inventory = {
    101: {
        "name": "Laptop",
        "category": "Electronics",
        "brand": ("Dell",),     
        "quantity": 5,
        "price": 799.99
    },
    102: {
        "name": "Mouse wireless",
        "category": "Electronics",
        "brand": ("Logitech",),
        "quantity": 25,
        "price": 29.99
    },
    103: {
        "name": "Monitor 24 inches",
        "category": "Electronics",
        "brand": ("Samsung",),        
        "quantity": 10,
        "price": 199.99
    },
    104: {
        "name": "Wood Desk",
        "category": "Office",
        "brand": ("IKEA",),     
        "quantity": 4,
        "price": 150.00
    },
    105: {
        "name": "Ergonomic chair",
        "category": "Office",
        "brand": ("Herman Miller",),
        "quantity": 2,
        "price": 899.50
    },
    106: {
        "name": "Table",
        "category": "Home",
        "brand": ("Philips",),        
        "quantity": 15,
        "price": 45.00
    },
    107: {
        "name": "Mechanical Keyboard",
        "category": "Electronics",
        "brand": ("Corsair",),
        "quantity": 20,
        "price": 89.99
    },
    108: {
        "name": "Booknote",
        "category": "Office",
        "brand": ("Moleskine",),
        "quantity": 50,
        "price": 15.00
    },
    109: {
        "name": "Coffe Maker",
        "category": "Home",
        "brand": ("Keurig",),
        "quantity": 8,
        "price": 120.00
    },
    110: {
        "name": "Microwave",
        "category": "Home",
        "brand": ("Panasonic",),
        "quantity": 3,
        "price": 150.00
    }
}
# List to Categories
categoriesList = ["Home", "Office", "Electronics"]

# Set to ID's
idSet = {101, 102, 103, 104, 105, 106, 107, 108, 109, 110}

# Functions

# Adding new item

addItemMenu = ""

def addItem():
    itemName = str(input("Enter product name: > "))
    while True:
        print("Select a Category")
        numC = 1
        for cat in categoriesList:
            print(f"{numC}. {cat}")
            numC = numC + 1

        itemCategory = int(input("> "))

        if 1 <= itemCategory <= len(categoriesList):
            itemCategory = categoriesList[itemCategory - 1]
            print(f"You selected {itemCategory}")
            break
        else:
            print("Select a correct option.")

    itemBrandint = str(input("Enter brand name: > "))
    itemBrand = (itemBrandint,)
    while True:
        try:
            itemQuantity = int(input("Enter quantity: > "))
            break
        except ValueError:
            print("Invalid input! \nPlease enter a integer number")
    while True:
        try:       
            itemPrice = float(input("Enter price: > "))
            break
        except ValueError:
            print("Invalid input! \nPlease enter a number (It can be a integer or float)")
    newId = max(inventory.keys()) + 1

    inventory[newId] = {
        "name": itemName,
        "category": itemCategory,
        "brand": itemBrand,
        "quantity": itemQuantity,
        "price": itemPrice
    }
    print("Item was added successfully")

def viewItem():
    print("Select an option")

    while True:
        numV = 1
        for i in inventory:
            print(f"{numV}. {i}")
            numV = numV + 1
        
        selectId = int(input("> "))

        if 1 <= selectId <= len(inventory):
            listIds = list(inventory.keys())
            selId = listIds[selectId - 1]
            
            nameDis = inventory[selId]["name"]
            brandDis = inventory[selId]["brand"]
            categoryDis = inventory[selId]["category"]
            priceDis = inventory[selId]["price"]
            quantityDis = inventory[selId]["quantity"]

            print(Product(selId, nameDis, brandDis, categoryDis, priceDis, quantityDis))

            break
        else:
            print("Please select a valid option!")

def deleteItem():
    print("Select an Id to remove item")



def test():
    for i in inventory:
        
        newId = max(inventory.keys()) + 1
        print(newId)

# Classes

class Product:
    def __init__(self, ids, name, brand, category, price, quantity):
        self.id = ids
        self.name = name
        self.brand = brand
        self.category = category
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Brand: {self.brand[0]} | Category: {self.category} | Price: {self.price} | Quantity: {self.quantity}"

# Console Printing
print(welcoming)
while(navType != 5):
    print(mainMenu)
    navType = int(input("Select an option: > "))

    if(navType==1):
        print("Add Item")
        addItem()

    
    if(navType==2):
        print("View Inventory")
        viewItem()
    
    if(navType==3):
        print("Update Item")
    
    if(navType==4):
        print("Remove Item")
        deleteItem()
    
    if(navType==5):
        print("Saving Inventory...")

