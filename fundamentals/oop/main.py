class User:
    #constructor
    def __init__ (self,name):
        self.name = name
        self.account_balance= 0

#make deposit methode
    def make_deposit(self,amount):
        self.account_balance += amount
#make withdrawl mthode
    def make_withdrawl(self,amount):
        self.account_balance-= amount
#display methode
    def display(self):
        print(f" User.{self.name}, Balance: ${self.account_balance}")

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
user1.make_deposit(300)
user1.make_deposit(200)
user1.make_deposit(400)
user1.make_withdrawl(100)

#display balances
user1.display()
user2.display()
user3.display()

# second user make 2 deposit and 2 withdrawls
user2.make_deposit(200)
user2.make_deposit(150)
user2.make_withdrawl(100)
user2.make_withdrawl(120)
#display balances
user1.display()
user2.display()
user3.display()

#third user make 1 deposit and 3 withdrawls
user3.make_deposit(1000)
user3.make_withdrawl(250)
user3.make_withdrawl(150) 
#display balances
user1.display()
user2.display()
user3.display()

#transfer money
user1.transfer_money(user2, 340)
user1.display()
user2.display()