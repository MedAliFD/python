class BankAccount:
    accounts = 0 #optional number of accounts
    accountsList=[]

    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance= balance
        BankAccount.accounts+= 1 # optional
        BankAccount.accountsList.append(self)


#methode to calculate number of accounts
    @classmethod
    def accountsNumber(cls):
        print(f" there are {cls.accounts} account(s)  created")
#deposit
    def deposit(self,amount):
        self.balance += amount
        return(self)
#withdrawl
    def withdrawl(self,amount):
        self.balance-= amount
        return(self)
#display
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
#interest 
    def yield_interest(self):
        if self.balance > 0 :
            self.balance= self.balance * (1+self.int_rate)
        else :
            print(f"can't apply interest on your balance which is {self.balance}$")
        return(self)
    

#print all instancesinfo
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accountsList:
            account.display_account_info()


#Assignemnt tasks
account1=BankAccount(0.2,500) # initialize the 1st account
account2=BankAccount(0.2,1000) # initialize the 1st account

account1.deposit(1000).deposit(800).deposit(300).withdrawl(100).yield_interest().display_account_info()
account2.deposit(300).deposit(700).withdrawl(100).withdrawl(100).withdrawl(100).withdrawl(100).yield_interest().display_account_info()
BankAccount.accountsNumber()

BankAccount.print_all_accounts()

