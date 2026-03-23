import json

# Messages
welcoming = "Welcome to the Inventory Management System"
mainMenu = "1. Add Item \n2. View Inventory \n3. Update Item \n4. Remove Item \n5. Exit"
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

try:
    with open("inventory.txt", "r") as file:
        inventory = json.load(file)

# Convert ID to integers 
        inventory = {int(k): v for k, v in inventory.items()}
except FileNotFoundError:
    pass

# List to Categories
categoriesList = ["Home", "Office", "Electronics"]

# Set to ID's
idSet = {101, 102, 103, 104, 105, 106, 107, 108, 109, 110}

# Functions

def selectID():
    while True:
        numV = 1
        for i in inventory:
            print(f"{numV}. {i}")
            numV = numV + 1
        
        try:
            selectId = int(input("> "))
            
            if 1 <= selectId <= len(inventory):
                listIds = list(inventory.keys())
                selId = listIds[selectId - 1]
                
                return selId 
            else:
                print("Please select a valid option!")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Adding new item

addItemMenu = ""

def addItem():
    try:
        while True:
            itemName = str(input("Enter product name: > "))
            if(itemName == ""):
                print("Please enter a name")
            else:
                break
    except ValueError:
        print("Wrong Command.")
    while True:
        print("Select a Category")
        numC = 1
        for cat in categoriesList:
            print(f"{numC}. {cat}")
            numC = numC + 1

        try:
            itemCategory = int(input("> "))

            if 1 <= itemCategory <= len(categoriesList):
                itemCategory = categoriesList[itemCategory - 1]
                print(f"You selected {itemCategory}")
                break
            else:
                print("Select a correct option.")
        except ValueError:
            print("Wrong Command!")

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

    idSet.add(newId)

    while True:
        try:
            periInput = int(input("Is this a persihable product?\n1. Yes\n2. No\n> "))
        except:
            print("Select a correct option.")
        if(periInput == 1):
            date = input("Enter expiration date: > ")
            break
        elif(periInput == 2):
            date = None
            break
        else:
            print("Select a correct option.")

    inventory[newId] = {
        "name": itemName,
        "category": itemCategory,
        "brand": itemBrand,
        "quantity": itemQuantity,
        "price": itemPrice,
        "expiration": date
    }
    print("Item was added successfully")

def viewItem():
    print("Select an option")
        
    selId = selectID()
    
    nameDis = inventory[selId]["name"]
    brandDis = inventory[selId]["brand"]
    categoryDis = inventory[selId]["category"]
    priceDis = inventory[selId]["price"]
    quantityDis = inventory[selId]["quantity"]

    expirationDate = inventory[selId].get("expiration")

    if expirationDate != None:
        
        print(PerishableProduct(selId, nameDis, brandDis, categoryDis, priceDis, quantityDis, expirationDate))
    else:
        
        print(Product(selId, nameDis, brandDis, categoryDis, priceDis, quantityDis))


def updateItem():
    print("Select an ID to update.")

    selId = selectID()

    while True:
        try:
            newQuantity = int(input("Enter quantity: > "))
            break
        except ValueError:
            print("Invalid input! \nPlease enter a integer number")
    while True:
        try:       
            newPrice = float(input("Enter price: > "))
            break
        except ValueError:
            print("Invalid input! \nPlease enter a number (It can be a integer or float)")

    nameUp = inventory[selId]["name"]
    brandUp = inventory[selId]["brand"]
    categoryUp = inventory[selId]["category"]
    priceUp = inventory[selId]["price"]
    quantityUp = inventory[selId]["quantity"]

    updateClass = Product(selId, nameUp, brandUp, categoryUp, priceUp, quantityUp)

    updateClass.updateDetails(newPrice, newQuantity)
    
    inventory[selId]["price"] = updateClass.price
    inventory[selId]["quantity"] = updateClass.quantity

    print(f"The item which ID is {selId} was update \nNew quantity: {inventory[selId]["quantity"]}\nNew price: {inventory[selId]["price"]}")


def deleteItem():
    print("Select an Id to remove item")

    selId = selectID()

    del inventory[selId]
    idSet.remove(selId)

    print(f"ID [{selId}] was deleted.")


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
    
    def updateDetails(self, newPrice, newQuantity):
        self.price = newPrice
        self.quantity = newQuantity

class PerishableProduct(Product):

    def __init__(self, ids, name, brand, category, price, quantity, expirationDate):
        super().__init__(ids, name, brand, category, price, quantity)

        self.expirationDate = expirationDate
    
    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Brand: {self.brand[0]} | Category: {self.category} | Price: {self.price} | Quantity: {self.quantity} | Expiration: {self.expirationDate}"

# Console Printing
print(welcoming)
while(navType != 5):
    print(mainMenu)
    try:
        navType = int(input("Select an option: > "))
    except ValueError:
        print("Wrong Command.")

    if(navType==1):
        print("Add Item")
        addItem()

    
    if(navType==2):
        print("View Inventory")
        viewItem()
    
    if(navType==3):
        print("Update Item")
        updateItem()
    
    if(navType==4):
        print("Remove Item")
        deleteItem()
    
    if(navType==5):
        print("Saving Inventory...")
        with open("inventory.txt", "w") as file:
            json.dump(inventory, file)

