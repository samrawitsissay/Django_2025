# 1, A shop gives a discount if a customer buys more than 3 items.
# Write a program that asks the user for the number of items they want
# to buy and prints: 
# "Discount applied" if items > 3
# "No discount" otherwise
num_items = int(input("Please enter number of items you want to buy: "))
try:
     if num_items>3:
        print("Discount applied")
     else:
        print("No discount")
     if num_items < 0: 
        raise ValueError("Number of items cannot be negative.")           
except ValueError:
        print("Invalid input. Please enter a valid number of items.")