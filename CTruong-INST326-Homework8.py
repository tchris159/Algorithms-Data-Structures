'''

INST326 Object-Oriented Programming
Section 0201
Homework 8
Christopher Truong
Fall 2017

'''



class BankAccount():
    def __init__(self, owner='unknown', checking=0, savings=0):
        self._owner = owner
        self._checking = checking
        self._savings = savings                #This function initializes the variables and calls self to store values

    def __str__(self):
        return "Owner: " + str(self._owner) + (", Checking Account: $" ) + str(self._checking) + ", Savings Account: $" + str(self._savings)     #String method returns the full line of the output with owner, savings, checking in string format

    def displayBalance(self):
        print (self._owner, round(self._checking, 2), round(self._savings, 2)) #This prints out the balance of the specified owner, checking and savings rounded to two. Essentially a dashboard that gives information
#in other words it accesses data but does not change anything
    def deposit(self, toChecking, toSavings): #This replicates a deposit.
        self._checking += toChecking
        self._savings += toSavings #The function is called and modifies the checking and savings by adding a specific amount (toChecking toSavings) to the current value

    def checking2savings(self, transfer):
        if self.checking >= transfer:    #insurance policy to make sure that the person has enough money to give a transfer
            self._checking -= transfer  #subtract money from checking
            self._savings += transfer #adds it to the savings account
        else:
            print("Insufficient funds.")   # if person doesn't have enough, it will produce error

    def __add__(self, other):
        total = BankAccount()
        total._owner = self._owner + " + " + other._owner          #new account joining the two owners
        total._checking = '${:,.2f}'.format(self._checking + other._checking)
        total._savings = '${:,.2f}'.format(self._savings + other._savings)
        return total     #totals the checking and savings all together and returns it


ba1 = BankAccount('Dimitri', 100.00, 50.00)
ba2 = BankAccount('Andrew', 150.00, 75.00)
ba1.displayBalance()

print(ba1 + ba2)




