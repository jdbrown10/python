class BankAccount:
    all_balances = []
    def __init__(self, balance, int_rate):
        self.amount = balance
        self.int_rate = int_rate
        self.balances_list = []
        self.balances_list.append(balance)
        BankAccount.all_balances.append(balance)
    def deposit(self, amount):
        self.amount += amount
        self.balances_list.append(self.amount)
        return self
    def withdraw(self, amount):
        self.amount -= amount
        self.balances_list.append(self.amount)
        return self
    def display_account_info(self):
        print(self.amount)
        return self
    def yield_interest(self):
        self.amount = self.amount + self.amount * self.int_rate
        self.balances_list.append(self.amount)
        return self
    def get_all_instances(self):
        print(self.balances_list)
    @classmethod
    def get_all_accounts(cls):
        print(cls.all_balances)

alexander = BankAccount(500, .01)
patches = BankAccount(3000, .03)

alexander.deposit(50).deposit(70).deposit(30).yield_interest().display_account_info()

BankAccount.get_all_accounts()
# patches.deposit(500).deposit(710).withdraw(300).withdraw(40).withdraw(500).withdraw(100).yield_interest().display_account_info()

alexander.get_all_instances()