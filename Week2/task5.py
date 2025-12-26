# 5,You receive a file called sales.txt where each line should contain a
# sales number.
# Example:
#  200
#  450
#  abc
#  700   
# Write a program that:
# a, Reads every line in sales.txt
# b, Converts valid lines into integers
# c, Skips invalid lines (like "abc") using exception handling
# d, Stores the valid numbers in a list
# e, Calculates and prints the total sales
valid_sales = []
with open("sales.txt", "r") as sales_file:          
    for line in sales_file:
        try:
            sale = int(line.strip())
            valid_sales.append(sale)
        except ValueError:
            continue    
total_sales = sum(valid_sales)
print("Total sales:", total_sales) 