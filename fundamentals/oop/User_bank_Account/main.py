class BankAccount:
    accounts=[]

    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance= balance
        BankAccount.accounts.append(self)

#deposit
    def deposit(self,amount):
        self.balance += amount
        print(f" Amount Deposited:, {amount} ")
        return self
#withdrawl
    def withdrawl(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print("You Withdrew:", amount)
        else:
            print("Insufficient Funds  ")
        return self

# #interest 
#     def yield_interest(self):
#         if self.balance > 0 :
#             self.balance +=  (self.balance *self.int_rate)
#         else :
#             print(f"can't apply interest on your balance which is {self.balance}$")
#         return self

#display
    def display_account_info(self):
        return f" ${self.balance}"

#print all instancesinfo
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:

    def __init__ (self,name):
        self.name = name
        self.account= {
            "checking" : BankAccount (0.05,0),
            "savings": BankAccount (.02,100)
            }
#display methode
    def display_users(self):
        print(f" User.{self.name}, Checking Balance : ${self.account['checking'].display_account_info()}")
        print(f" User.{self.name}, Saving Balance: ${self.account['savings'].display_account_info()}")
adrien=User("adrien")
adrien.account['checking'].deposit(100)
adrien.display_users()




# BankAccount.print_all_accounts()

