# BankAccount Class 
# ● Create a class BankAccount with private balance. 
# ● Add methods deposit(), withdraw(), and get_balance(). 
# ● Ensure withdraw() does NOT allow negative balance. 
# ● Test by attempting an invalid withdrawal. 
class BankAccount:
    def __init__(self):
        self.__balance = 0       
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount     
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds. Withdrawal denied.")
        elif amount > 0:
            self.__balance -= amount     
    def get_balance(self):
        return self.__balance


account = BankAccount()
account.deposit(100)
account.withdraw(150)  
print(account.get_balance())