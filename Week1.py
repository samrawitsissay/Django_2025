#create a program that asks your age and prints your age
age = input("Please enter your age: ")
if age>0:
    print("Your age is:", age)

#write a program that checks if a number is even or odd
number=int(input("Enter a number:"))
if number%2 ==0:
    print("The number is even.")
else:
    print("The number is odd.")

#jwrite a program that calculates the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)    
    

#write a program that prints a maximum number in a list
numbers = [3, 5, 2, 8, 1]
max_number = max(numbers)
print("The maximum number in the list is:", max_number)

