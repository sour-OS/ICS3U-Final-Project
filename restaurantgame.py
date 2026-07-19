'''restaurantgame.py

Sourodeep Bhowmik
 2026/07/17
 program description:  Final Project - Restaurant Game

'''

#-------------------------------------------------------------------
# imports
import random

#-------------------------------------------------------------------
# global variables
userInput = 1
breakfastItems = ["Pancakes", "Waffles", "Omelet"]      # breakfast item list
breakfastPrices = [4.00, 4.50, 4.25]                 # breakfast item prices list
lunchItems = ["Steak", "Chicken Parmesan", "Vegetable Stir Fry"]      # lunch item list
lunchPrices = [8.99, 10.50, 6.75]                 # lunch item prices list
dinnerItems = ["Salmon", "Beef Tenderloin", "Vegetarian Lasagna"]      # dinner item list
dinnerPrices = [12.99, 15.50, 9.75]                 # dinner item prices list
dessertItems = ["Cheesecake", "Chocolate Cake", "Ice Cream"]      # dessert item list
dessertPrices = [4.50, 5.00, 3.25]
drinkItems = ["Soda", "Coffee", "Tea"]      # drinks item list
drinkPrices = [1.50, 2.00, 1.75]
orderList = []                                    # holds ordered item tuples
totalCost = 0                                     # running subtotal
TAX_RATE = 0.08

#-------------------------------------------------------------------
# modules

def greetings():
    print("Welcome to Souro's Diner!\n")

def show_main_menu():
    print("Main Menu\n")
    print("\t1. Order Food")
    print("\t0. Exit\n")

def show_menu(itemList, priceList):
    print("Menu\n")
    for i in range(len(itemList)):
        print(f"\t{i+1}. {itemList[i]} - ${priceList[i]:.2f}")
    print("\t0. Checkout / Exit\n")

def choose_category():
    valid = False
    while valid == False:
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
    global totalCost  # need this since we're changing the global variable

    # --- validate item choice ---
    validChoice = False
    while validChoice == False:
        raw = input("Enter item number: ")
        if raw.isdigit() and 1 <= int(raw) <= len(itemList):
            choice = int(raw) - 1  # convert to list index
            validChoice = True
        else:
            print("Invalid item number, try again.\n")

    # --- validate quantity ---
    validQty = False
    while validQty == False:
        raw = input("How many? ")
        if raw.isdigit() and int(raw) > 0:
            qty = int(raw)
            validQty = True
        else:
            print("Enter a whole number greater than 0.\n")

    # --- arithmetic: add to order ---
    orderList.append((itemList[choice], priceList[choice], qty))
    totalCost = totalCost + (priceList[choice] * qty)
    print(f"Added {qty} x {itemList[choice]} to your order.\n")

def print_receipt():
    print("----- Receipt -----")
    for name, price, qty in orderList:
        line_total = price * qty
        print(f"{name} x {qty} - ${line_total:.2f}")
    tax = totalCost * TAX_RATE
    print(f"Subtotal: ${totalCost:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${totalCost + tax:.2f}")

def bye():
    print("Thanks for ordering with us!\n")
    print_receipt()

#-------------------------------------------------------------------
# main code

greetings()
while userInput != 0:
    show_main_menu()
    userInput = int(input("What would you like to do?\n"))
    match userInput:
        case 1:
            items, prices = choose_category()
            show_menu(items, prices)
            take_order(items, prices)
        case 0:
            break
        case other:
            print("Not a valid option!\n")

bye()
