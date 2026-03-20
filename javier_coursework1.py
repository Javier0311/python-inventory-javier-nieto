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
    itemName = str(input("Enter product name: "))
    while True:
        print("Select a Category")
        numC = 1
        for cat in categoriesList:
            print(f"{numC}. {cat}")
            numC = numC + 1

        itemCategory = int(input())

        if 1 <= itemCategory <= len(categoriesList):
            itemCategory = categoriesList[itemCategory - 1]
            print(f"You selected {itemCategory}")
            break
        else:
            print("Select a correct option.")

    itemBrandint = str(input("Enter brand name: "))
    itemBrand = (itemBrandint,)
    while True:
        try:
            itemQuantity = int(input("Enter quantity: "))
            break
        except ValueError:
            print("Invalid input! \nPlease enter a integer number")
    while True:
        try:       
            itemPrice = float(input("Enter price: "))
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


def test():
    for i in inventory:
        
        newId = max(inventory.keys()) + 1
        print(newId)
    

# Console Printing
print(welcoming)
while(navType != 5):
    print(mainMenu)
    navType = int(input("Please select an option: "))

    if(navType==1):
        print("Add Item")
        addItem()

    
    if(navType==2):
        print("View Inventory")
        test()
    
    if(navType==3):
        print("Update Item")
    
    if(navType==4):
        print("Remove Item")
    
    if(navType==5):
        print("Saving Inventory...")

