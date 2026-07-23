'''
restaurantgame.py
Sourodeep Bhowmik
2026/07/17

Final Project – Restaurant Ordering Game
'''

#-------------------------------------------------------------------
# imports, random used to generate a starting budget
import random

#-------------------------------------------------------------------
# global variables: store game state such as budget, people count, menu items, prices, order list, and running totals

userInput = 1

budget = random.randint(25, 75)  # random starting money
peopleCount = int(input("How many people are in your party? "))  # user input
itemsNeeded = peopleCount * 2  # each person needs 2 items
moneyRemaining = budget  # track remaining money
itemsPurchased = 0  # track how many items have been bought

# menu item lists
breakfastItems = ["Idli & Dosa", "Paratha", "Eggroll"]
breakfastPrices = [4.00, 4.50, 4.25]

lunchItems = ["Pulao", "Dal Tadka", "Rajma"]
lunchPrices = [7.99, 8.50, 6.75]

dinnerItems = ["Biriyani", "Khichdi", "Butter Chicken"]
dinnerPrices = [12.99, 15.50, 9.75]

dessertItems = ["Gulab Jamun", "Rasgulla", "Kheer"]
dessertPrices = [4.50, 5.00, 3.25]

drinkItems = ["Soda", "Coffee", "Tea"]
drinkPrices = [1.50, 2.00, 1.75]

orderList = []  # stores ordered items
totalCost = 0  # running subtotal
TAX_RATE = 0.08  # constant tax rate

#-------------------------------------------------------------------
# modules
def greetings():
    # Prints welcome message and shows the user's starting budget and item requirement
    print("Welcome to Souro's Diner!\n")
    print(f"Your budget is: ${budget:.2f}")
    print(f"You need to buy {itemsNeeded} total items for your party.\n")

def show_main_menu():
    # Displays the main menu options for the user
    print("Main Menu\n")
    print("\t1. Order Food")
    print("\t2. Check Budget / People Status")
    print("\t0. Checkout / Exit\n")

def show_menu(itemList, priceList):
    # Shows the selected category's items and prices
    print("Menu\n")
    for i in range(len(itemList)):
        print(f"\t{i+1}. {itemList[i]} - ${priceList[i]:.2f}")
    print("\t0. Go Back\n")

def choose_category():
    # Asks the user to choose a food category and returns the correct item/price lists
    valid = False
    while not valid:
        cat = input("Choose a category (breakfast/lunch/dinner/desserts/drinks): ").lower()
        if cat == "breakfast":
            return breakfastItems, breakfastPrices
        elif cat == "lunch":
            return lunchItems, lunchPrices
        elif cat == "dinner":
            return dinnerItems, dinnerPrices
        elif cat == "desserts":
            return dessertItems, dessertPrices
        elif cat == "drinks":
            return drinkItems, drinkPrices
        else:
            print("Not a valid category, try again.\n")

def take_order(itemList, priceList):
    # Handles ordering: validates item number and quantity, checks if the user can afford the purchase, updates totals, money remaining, and items purchased

    global totalCost, moneyRemaining, itemsPurchased

    # --- validate item choice ---
    validChoice = False
    while not validChoice:
        raw = input("Enter item number: ")
        if raw.isdigit() and 1 <= int(raw) <= len(itemList):
            choice = int(raw) - 1
            validChoice = True
        else:
            print("Invalid item number, try again.\n")

    # --- validate quantity ---
    validQty = False
    while not validQty:
        raw = input("How many? ")
        if raw.isdigit() and int(raw) > 0:
            qty = int(raw)
            validQty = True
        else:
            print("Enter a whole number greater than 0.\n")

    # --- calculate cost ---
    itemCost = priceList[choice] * qty

    # --- check if user can afford ---
    if itemCost > moneyRemaining:
        print(f"You cannot afford {qty} x {itemList[choice]}.\n")
        return

    # --- update totals ---
    orderList.append((itemList[choice], priceList[choice], qty))
    totalCost += itemCost
    moneyRemaining -= itemCost
    itemsPurchased += qty

    print(f"Added {qty} x {itemList[choice]} to your order.\n")

def print_receipt():
    # Prints the final receipt including itemized costs, tax,
    # total, budget summary, and success/failure message

    print("\n----- Receipt -----")
    for name, price, qty in orderList:
        line_total = price * qty
        print(f"{name} x {qty} - ${line_total:.2f}")

    tax = totalCost * TAX_RATE
    finalTotal = totalCost + tax

    print(f"\nSubtotal: ${totalCost:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${finalTotal:.2f}")

    print("\n----- Summary -----")
    print(f"Budget: ${budget:.2f}")
    print(f"Money Remaining: ${moneyRemaining:.2f}")
    print(f"People in Party: {peopleCount}")
    print(f"Items Needed: {itemsNeeded}")
    print(f"Items Purchased: {itemsPurchased}")

    if itemsPurchased >= itemsNeeded:
        print("\nYou successfully purchased enough items for your party!")
    else:
        print(f"\nYou did NOT purchase enough items. You were short by {itemsNeeded - itemsPurchased} items.")

        # --- save receipt to external file ---
    with open("receipt.txt", "a") as file:
        file.write("----- Receipt -----\n")
        for name, price, qty in orderList:
            line_total = price * qty
            file.write(f"{name} x {qty} - ${line_total:.2f}\n")

        tax = totalCost * TAX_RATE
        finalTotal = totalCost + tax

        file.write(f"\nSubtotal: ${totalCost:.2f}\n")
        file.write(f"Tax: ${tax:.2f}\n")
        file.write(f"Total: ${finalTotal:.2f}\n")

        file.write("\n----- Summary -----\n")
        file.write(f"Budget: ${budget:.2f}\n")
        file.write(f"Money Remaining: ${moneyRemaining:.2f}\n")
        file.write(f"People in Party: {peopleCount}\n")
        file.write(f"Items Needed: {itemsNeeded}\n")
        file.write(f"Items Purchased: {itemsPurchased}\n")

        if itemsPurchased >= itemsNeeded:
            file.write("Status: Success — enough items purchased.\n\n")
        else:
            file.write(f"Status: Failure — short by {itemsNeeded - itemsPurchased} items.\n\n")

        # --- automatically open the receipt file ---
        import os
        os.startfile("receipt.txt")


def bye():
    # Prints a goodbye message and calls the receipt function
    print("\nThanks for ordering with us!\n")
    print_receipt()

#-------------------------------------------------------------------
# main code

greetings()

while userInput != 0:
    show_main_menu()
    userInput = int(input("What would you like to do?\n"))

    match userInput:
        case 1:
            # User chooses to order food
            items, prices = choose_category()
            show_menu(items, prices)
            take_order(items, prices)

            # enforce item requirement
            if itemsPurchased < itemsNeeded:
                print(f"You still need {itemsNeeded - itemsPurchased} more items.\n")

            # enforce money fail condition
            if moneyRemaining <= 0 and itemsPurchased < itemsNeeded:
                print("You ran out of money before serving everyone!\n")
                break

        case 2:
            # Show current budget and progress
            print(f"\nBudget: ${budget:.2f}")
            print(f"People in party: {peopleCount}")
            print(f"Items needed: {itemsNeeded}")
            print(f"Money remaining: ${moneyRemaining:.2f}")
            print(f"Items purchased: {itemsPurchased}\n")

        case 0:
            # Prevent checkout if user hasn't bought enough items
            if itemsPurchased < itemsNeeded:
                print(f"You cannot checkout yet! You still need {itemsNeeded - itemsPurchased} more items.\n")
                userInput = 1  # send user back to menu
            else:
                break

        case _:
            print("Not a valid option!\n")

bye()
input("Press Enter to exit...")
