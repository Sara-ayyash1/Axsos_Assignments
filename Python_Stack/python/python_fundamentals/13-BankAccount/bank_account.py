class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0 ):
        self.int_rate = int_rate 
        self.balance = balance
   
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
           self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print (f"Balance: ${self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

# Create 2 accounts
account1 =  BankAccount(0.02 , 3000)
account2 = BankAccount(10)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
account1.deposit(100).deposit(100).deposit(700).withdraw(100).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
account2.deposit(5).deposit(400).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()
