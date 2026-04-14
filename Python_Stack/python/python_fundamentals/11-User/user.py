class User:
    def __init__(self , name , balance):
        self.name = name
        self.balance = balance

    def make_deposit(self , amount):
        self.balance += amount

    def make_withdrawal(self , amount):
        self.balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")

    def transfer_money(self,other_user,amount):
        self.balance -=amount
        other_user.balance +=amount
    
# Create 3 instances of the User class
user1 = User ("Sara Ayyash" , 1000)
user2 = User ("Islam" , 30000)
user3 = User ("Haya" , 800)

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
user1.make_deposit(100)
user1.make_deposit(200)
user1.make_deposit(50)
user1.make_withdrawal(50)
user1.display_user_balance()

# Have the second user make 2 deposits and 2 withdrawal and then display their balance
user2.make_deposit(100)
user2.make_deposit(100)
user2.make_withdrawal(50)
user2.make_withdrawal(100)
user2.display_user_balance()

# Have the third user make 1 deposits and 3 withdrawal and then display their balance
user3.make_deposit(500)
user3.make_withdrawal(100)
user3.make_withdrawal(100)
user3.make_withdrawal(50)
user3.display_user_balance()

#  Add a transfer_money method => have the first user transfer money to the third user and then print both users' balances
user1.transfer_money(user3, 200)
user1.display_user_balance()
user3.display_user_balance()