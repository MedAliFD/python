class User:
    #constructor
    number=0

    def __init__ (self,name):
        self.name = name
        self.account_balance= 0
        User.number += 1
        self.index=User.number

#make deposit methode
    def make_deposit(self,amount):
        self.account_balance += amount
        return(self)
#make withdrawl mthode
    def make_withdrawl(self,amount):
        self.account_balance-= amount
        return(self)
#display methode
    def display(self):
        print(f" User #{self.index} {self.name}, Balance: ${self.account_balance}")

#transfert methode
    def transfer_money(self, recipient,amount):
        self.account_balance -= amount
        recipient.account_balance += amount
        print(f" A transefer of {amount}$ from {self.name} to {recipient.name} has been applied")

# three instance for the class User
user1=User("Med")
user2=User("Ali")
user3=User("Dali")

#first user make 3 deposits and 1 withdrawl
user1.make_deposit(300).make_deposit(200).make_deposit(400).make_withdrawl(100).display()

#display balances
user2.display()
user3.display()

# second user make 2 deposit and 2 withdrawls
user2.make_deposit(200).make_deposit(150).make_withdrawl(100).make_withdrawl(120).display()
#display balances
user1.display()
user3.display()

#third user make 1 deposit and 3 withdrawls
user3.make_deposit(1000).make_withdrawl(250).make_withdrawl(150) .display()
#display balances
user1.display()
user2.display()
user3.display()

#transfer money
user1.transfer_money(user2, 340).display()
user2.display()