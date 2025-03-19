class BankAccount:
    def __init__(self,ssn,name,balance,phone="",email=""):
        self.name = name
        self.ssn = ssn
        self.balance = balance
        self.phone = phone
        self.email = email

    def account_balance(self):
        return self.balance

    def deposit(self,deposit_amt):
        if deposit_amt > 0:
            self.balance += deposit_amt
        return self.balance

    def withdraw(self, withdraw_amt):
        if 0 < withdraw_amt < self.balance:
            self.balance -=withdraw_amt
        else:
            print(f"The balance amount: {self.balance} and withdraw amount:{withdraw_amt} , Sorry can not withdraw money from your account")
        return self.balance


account1 = BankAccount(234-456-754, "ved",5000,"230-345-3222","ved@gmail.com")

print(f"Your current balance is : {account1.account_balance()}")
print(f"Account Balance after deposit : {account1.deposit(500)}")
print(f"Account Balance after withdraw : {account1.withdraw(1500)}")