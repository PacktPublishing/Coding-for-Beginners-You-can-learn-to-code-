"""
Munch App MVP
By Applause

The purpose of Munch is to produce a dinner menu from favorite dishes and produce a shopping list of ingredients if required.
"""
# ----Imports----
from random import choice

# ----A. Functions----

# A1. Choose dishes
def chooseDishes(days):
    while len(myMenu) < int(days):
        chosenDish = choice(foodWeLike)
        if chosenDish not in myMenu:
            myMenu.append(chosenDish)
    print("Done! Here's your menu...")
    print()
    for dish in myMenu:
        print(dish)
    print()
    print(f"Out of all these dishes, my favourite has to be... {choice(myMenu)}")

# A2. Build shopping list
def buildShoppingList():
    myShoppingList = []
    
    if "Pizza" in myMenu:
        myShoppingList.append(pizza)
    if "Beef Burgers" in myMenu:
        myShoppingList.append(BeefBurgers)
    if "Pork Stir Fry" in myMenu:
        myShoppingList.append(PorkStirFry)
    if "Chicken Fajitas" in myMenu:
        myShoppingList.append(ChickenFajitas)
    if "Bangers and Mash" in myMenu:
        myShoppingList.append(BangersMash)
    if "Fish and Chips" in myMenu:
        myShoppingList.append(FishChips)
    if "Spanish Omelette" in myMenu:
        myShoppingList.append(SpanishOmelette)
    
    # Print the shopping list
    print()
    for dish in myShoppingList:
        for ingredient in dish:
            print(ingredient)
    print()
    print("Voila! Bon Appetit!")

# ---- B. Lists----
foodWeLike = ["Pizza", "Beef Burgers", "Pork Stir Fry", "Chicken Fajitas", "Bangers and Mash", "Fish and Chips", "Spanish Omelette"]

pizza = ["Pizza Base", "Tomato Sauce", "Cheese", "Pepperoni", "Chillis"]
BeefBurgers = ["Beef Patties", "Burger Rolls", "Lettuce", "Tomatoes", "Relish"]
PorkStirFry = ["Pork Loin", "Soy Sauce", "Noodles", "Vegetables"]
ChickenFajitas = ["Chicken Breast", "Red Peppers", "Onion", "Fajita Kit"]
BangersMash = ["Sausages", "Mashed Potatoes", "Gravy", "Onion", "Peas"]
FishChips = ["Fish", "Potatoes", "Tartar Sauce", "Peas"]
SpanishOmelette = ["Eggs", "Chorizo", "Baby Potatoes", "Peppers", "Onion"]

myMenu = []

# 1. How many days to plan?
print("Hello, I'm Munch! I'll help you plan your dinner menu...")

answer = input("How many days would you like me to plan? ")

print("OK, I'm going to plan " + answer + "dinner(s) from your favourite meals list")

# 2. Choose dishes
chooseDishes(answer)


# 3. Build shopping list
answer = input("Would you like a shopping list for these meals? ")
if answer == 'y':
    buildShoppingList()
else:
    print()
    print("You got it! Bye for now :)")
    

