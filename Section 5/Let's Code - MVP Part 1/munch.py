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

# A2. Build shopping list

# ---- B. Lists----
foodWeLike = ["Pizza", "Beef Burgers", "Pork Stir Fry", "Chicken Fajitas", "Bangers and Mash", "Fish and Chips", "Spanish Omelette"]
myMenu = []

#1. How many days to plan?
print("Hello, I'm Munch! I'll help you plan your dinner menu...")

answer = input("How many days would you like me to plan? ")

print(f"OK, I'm going to plan {answer} dinner(s) from your favourite meals list")

#  2. Choose dishes
chooseDishes(answer)
print("Done! Here's your menu...")
print()
print(myMenu)
print()
print(f"Out of all these dishes, my favourite has to be... {choice(myMenu)}")

#3. Build shopping list?