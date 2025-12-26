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