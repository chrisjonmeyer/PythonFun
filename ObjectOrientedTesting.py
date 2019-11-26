# Object Oriented Homework From Bootcamp
# Use https://github.com/Pierian-Data/Complete-Python-3-Bootcamp

# Create a class with methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
# class Line:

#     def __init__(self,coor1,coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
    
#     def distance(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coor2
#         return ((x2-x1)**2 + (y2-y1)**2)**0.5

#     def slope(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coor2
#         return (y2-y1)/(x2-x1)

# coordinate1 = (3,2)
# coordinate2 = (8,10)
# li = Line(coordinate1, coordinate2)
# print(li.distance())
# print(li.slope())



# For this challenge, create a bank account class that has two attributes:

# owner
# balance
# and two methods:

# deposit
# withdraw
# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,deposit_amount):
        self.balance += deposit_amount
        print("Deposit accepted")

    def withdraw(self,withdraw_amount):
        if (withdraw_amount < self.balance):
            self.balance -= withdraw_amount
            print("Withdrawl accepted")
        else:
            print("Insufficent Funds. Withdrawl declined")
    
    # Use this to override the string interpretation of the class to change what happens when you print the object
    def __str__(self):
        return f"Account Owner: {self.owner}\nAccount Balance: ${self.balance}"


acct1 = Account('Chris',100)
print(acct1)
acct1.deposit(50)
acct1.withdraw(100)
acct1.withdraw(100)
print(acct1)