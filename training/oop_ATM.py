class Account:
    
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner} \n Account balance: ${self.balance}"    
    
    def deposit(self, amount):
        self.balance += amount
        print('Deposit accepted!!!')

    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')



acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)

acct1.withdraw(70)

acct1.withdraw(705)
print(acct1.balance)

