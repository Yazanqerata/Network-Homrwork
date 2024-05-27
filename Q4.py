class BankAccount:
    def __init__(self, account_number, account_holder,balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance=balance

    def deposit(self, amount):
        self.balance += amount
        print('deposited $',amount,'into account',self.account_number,'and balance now is:$',self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print('Withdrew $',amount,'from account',self.account_number,'and balance now is :$',self.balance)
        else:
            print("'sorry' you don't have enough money")

    def get_balance(self):
        return self.balance

bank_account = BankAccount('2706', 'Yazan Qerata')

bank_account.deposit(1000)

bank_account.withdraw(500)

print('balance now is :$', bank_account.get_balance())

class SavingsAccount(BankAccount):
    def __init__(self,account_number,account_holder,balance,interest_rate):
        super().__init__(account_number, account_holder,balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print('Applied',self.interest_rate * 100,'% interest and balance now is :',self.balance)

    def __str__(self):
        return('Account Number: ' + str(self.account_number) + ' Account Holder: ' + str(self.account_holder) +' Balance: ' + str(self.balance) + ' Interest Rate: ' + str(self.interest_rate * 100) +'%')

savings_account = SavingsAccount('2706','Yazan Qerata',500,0.05)

savings_account.apply_interest()
print(savings_account)