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
# 2, You are given a list of product prices:
# prices = [120, 45, 300, 85, 150]
# Write a function get_expensive_products(prices) that returns a new
# list containing only the prices greater than 100.     
def get_expensive_products(prices):
    prices = [120, 45, 300, 85, 150]
    new_prices = []
    for price in prices:
        if price > 100:
            new_prices.append(price)    
    return new_prices
expensive_products = get_expensive_products([120, 45, 300, 85, 150])
print("Expensive products:", expensive_products)
#  3, Write a script that logs user activity.
#      When the program runs
#      Write "User logged in" to a file called log.txt.
#      Then read the file and print the full log history.
with open("log.txt", "a") as log_file:
    log_file.write("User logged in\n")
with open("log.txt", "r") as log_file:
    log_history = log_file.read()
print("Log history:")
print(log_history)