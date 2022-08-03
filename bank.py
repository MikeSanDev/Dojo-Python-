class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Not enough cheddar: There are no free-BRIEs")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: + {self.balance}")
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += (self.balance * self.int_rate)
        return self


savings = BankAccount(.05, 1000)
checking = BankAccount(.02, 5000)

savings.deposit(10).deposit(20).deposit(30).withdraw(
    500).yield_interest().display_account_info()
checking.deposit(1000).deposit(2000).deposit(4000).withdraw(
    500).yield_interest().display_account_info()
