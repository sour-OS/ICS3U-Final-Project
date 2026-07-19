'''Final Project - Restaurant Game

Sourodeep Bhowmik
 2026/07/17
 program description: ICS3U Final Project - Restaurant Game

'''

#-------------------------------------------------------------------
# imports
import random

#-------------------------------------------------------------------
# global variables
userInput = 1
mainDishes = ["Dish A", "Dish B", "Dish C"]      # main dish dictionary
mainPrices = [8.99, 10.50, 6.75]                 #main dish dictionary
orderList = []                                    # holds indexes of ordered items
totalCost = 0                                     # running subtotal
TAX_RATE = 0.08

#-------------------------------------------------------------------
# modules

def greetings():
    print("Welcome to Souro's Diner!\n")

def show_menu():
    print("Menu\n")
    for i in range(len(mainDishes)):  # loop through menu items
        print(f"\t{i+1}. {mainDishes[i]} - ${mainPrices[i]:.2f}")
    print("\t0. Checkout / Exit\n")

def take_order():
    global totalCost  # need this since we're changing the global variable

    # --- validate item choice ---
    validChoice = False
    while validChoice == False:
        raw = input("Enter item number: ")
        if raw.isdigit() and 1 <= int(raw) <= len(mainDishes):
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
    for i in range(qty):          # add one entry per quantity ordered
        orderList.append(choice)
    totalCost = totalCost + (mainPrices[choice] * qty)
    print(f"Added {qty} x {mainDishes[choice]} to your order.\n")

def print_receipt():
    print("----- Receipt -----")
    for i in orderList:
        print(f"{mainDishes[i]} - ${mainPrices[i]:.2f}")
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
    show_menu()
    userInput = int(input("What would you like to do?\n"))
    match userInput:
        case 1:
            take_order()
        case 0:
            break
        case other:
            print("Not a valid option!\n")

bye()
