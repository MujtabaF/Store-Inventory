inventory = {}
buyingp = {}
sellingp = {}
profit = 0
inventoryval = 0

def add(name, quantity, price, selling_price,inventoryval):
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity
        buyingp[name] = price
        sellingp[name] = selling_price
        inventoryval += quantity * price

def remove(name, inventoryval):
    i2 = inventory.copy()
    if name in i2:
        inventoryval -= inventory[name] * sellingp[name]
        del inventory[name]
        del buyingp[name]
        del sellingp[name]
    else:
        print("Item not in inventory")

def sell(name, quantity):
    global profit
    if name in inventory:
        if quantity <= inventory[name]:
            inventory[name] -= quantity
            profit += quantity * (sellingp[name]-buyingp[name])
        else:
            print("Quantity Exceeded")
    else:
        print("Item not in inventory")

def stock(name, quantity, inventoryval):
    if name in inventory:
        inventory[name] += quantity
        inventoryval += quantity * sellingp[name]
    else:
        print("This item is not in the inventory")

def total_value(inventory, selling):
    total = 0
    for key in inventory:
        total += inventory[key] * selling[key]
    print("The total Monetary value of the inventory right now is: ", total)

def calculate_profit():
    global profit
    currentProfit = profit - inventoryval 
    if currentProfit >= 0:
        print("Your profit as of now is:", currentProfit)
    else:
        print("Your loss as of now is:", -currentProfit)



while True:
    print("1: ADD")
    print("2: REMOVE")
    print("3: SELL")
    print("4: ADDING STOCK")
    print("5: DISPLAY THE MONETARY VALUE OF YOUR INVENTORY")
    print("6: THE PROFIT YOU HAVE MADE")
    print("7: TO END THE SERVICE")


    n = int(input("Enter the number in relation to what you want to do: "))
    if n == 1 :
        name = input("Enter the name of the item: ")
        quantity = float(input("Enter the quantity of the item: "))
        price = float(input("Enter the price: "))
        selling_price = float(input("Enter the selling price of your item: "))
        add(name, quantity, price, selling_price, inventoryval)
    elif n == 2:
        name = input("Enter the item you want to be deleted: ")
        remove(name, inventoryval)
    elif n == 3:
        name = input("Enter the name of the item you want to sell: ")
        quantity = float(input("Enter the quantity of the items sold: "))
        sell(name, quantity)
    elif n == 4:
        name = input("Enter the name of the item you want to restock: ")
        quantity = float(input("Enter the quantity of the items: "))
        stock(name, quantity, inventoryval)
    elif n == 5:
        total_value(inventory, buyingp)
    elif n == 6:
        calculate_profit()
    elif n == 7:
        print("Thanks for using this service")
        break

    print("Your current inventory is:", inventory)
    print()