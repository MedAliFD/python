class BankAccount:


    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance= balance

    
    def deposit(self,amount):
        self.balance += amount
        return(self)

    def withdrawl(self,amount):
        self.balance-= amount
        return(self)

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        if self.balance > 0 :
            self.balance= self.balance * (1+self.int_rate)
        else :
            print(f"can't apply interest on your balance which is {self.balance}$")
        return(self)

account1=BankAccount(0.2,500)
account2=BankAccount(0.2,1000)
account1.deposit(1000).deposit(800).deposit(300).withdrawl(100).yield_interest().display_account_info()
account2.deposit(300).deposit(700).withdrawl(100).withdrawl(100).withdrawl(100).withdrawl(100).yield_interest().display_account_info()

