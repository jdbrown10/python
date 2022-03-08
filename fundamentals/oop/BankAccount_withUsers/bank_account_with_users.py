class BankAccount:
    all_balances = []
    def __init__(self, balance, int_rate):
        self.amount = balance
        self.int_rate = int_rate
        self.balances_list = []
        self.balances_list.append(balance)
        BankAccount.all_balances.append(balance)
    @classmethod
    def get_all_accounts(cls):
        print(cls.all_balances)

class User:
    def __init__(self, name, balance, int_rate, balance2, int_rate2):
        self.name = name
        self.BankAccount1 = BankAccount(balance, int_rate)
        self.BankAccount2 = BankAccount(balance2, int_rate2)
    def deposit1(self, amount):
        self.BankAccount1.amount += amount
        self.BankAccount1.balances_list.append(self.BankAccount1.amount)
        return self
    def deposit2(self, amount):
        self.BankAccount2.amount += amount
        self.BankAccount2.balances_list.append(self.BankAccount2.amount)
        return self
    def withdraw1(self, amount):
        self.BankAccount1.amount -= amount
        self.BankAccount1.balances_list.append(self.BankAccount1.amount)
        return self
    def withdraw2(self, amount):
        self.BankAccount2.amount -= amount
        self.BankAccount2.balances_list.append(self.BankAccount2.amount)
        return self
    def yield_interest1(self):
        self.BankAccount1.amount = self.BankAccount1.amount + self.BankAccount1.amount * self.BankAccount1.int_rate
        self.BankAccount1.balances_list.append(self.BankAccount1.amount)
        return self
    def yield_interest2(self):
        self.BankAccount2.amount = self.BankAccount2.amount + self.BankAccount2.amount * self.BankAccount1.int_rate
        self.BankAccount2.balances_list.append(self.BankAccount2.amount)
        return self
    def display_account_info1(self):
        print(self.BankAccount1.amount)
        return self
    def display_account_info2(self):
        print(self.BankAccount2.amount)
        return self

alexander = User("Alexander", 500, .01, 3000, .03)

alexander.deposit1(50).deposit1(70).deposit1(30).yield_interest1().display_account_info1()
alexander.deposit2(50).deposit2(70).deposit2(30).yield_interest2().display_account_info2()