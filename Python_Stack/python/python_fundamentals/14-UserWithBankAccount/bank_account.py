class User:
    def __init__(self , name , email):
        self.name = name
        self.email = email
        self.accounts = []

    def make_deposit(self, amount, account_index=0):
        self.accounts[account_index].deposit(amount)
        return self

    def make_withdrawal(self, amount, account_index=0):
        self.accounts[account_index].withdraw(amount)
        return self

    def display_user_balance(self):
        for account in self.accounts:
            print(f"User: {self.name}, Balance: ${account.balance}")
        return self

    def transfer_money(self, amount, from_acc_index, other_user, to_acc_index):
        self.make_withdrawal(amount, from_acc_index)
        other_user.make_deposit(amount, to_acc_index)
        return self
    
    def open_new_account(self, int_rate = 0.01, balance = 0):
        new_account = BankAccount(int_rate, balance)
        self.accounts.append(new_account)
        return self
    

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


#Testing...

sara = User("Sara Ayyash", "sara@gmail.com")
sama = User("Sama", "sama@example.com")

sara.open_new_account(balance=100) 
sara.open_new_account(balance=1000) 
sama.open_new_account(0.01, 500)

sara.make_deposit(500, 0)     
sara.make_withdrawal(200, 1)  
sara.transfer_money(300, 0, sama, 0)

sara.display_user_balance()
sama.display_user_balance()