def get_expensive_product(prices):
    prices = [120, 45, 300, 85, 150]
    new_prices = []
    for price in prices:
        if price > 100:
            new_prices.append(price)    
    return print("Expensive products:", new_prices)