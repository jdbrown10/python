class User:
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account_balance = account_balance
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)
        return self
    def transfer_money_to_rykard(self, amount):
        self.account_balance -= amount
        rykard.account_balance += amount
        return self
    def transfer_money_to_someone(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

margit = User("margit", "margit@fellomen.ring", 400)
rennala = User("rennala", "rennala@respec", 1000)
rykard = User("rykard", "rykard@bigyucky", 0)

margit.make_deposit(100).make_deposit(50).make_deposit(125).make_withdrawal(125).display_user_balance()

rennala.make_deposit(300).make_deposit(200).make_withdrawal(700).make_withdrawal(2).display_user_balance()

rykard.make_deposit(10).make_withdrawal(2).make_withdrawal(3).make_withdrawal(1).display_user_balance()

margit.transfer_money_to_someone(rykard, 90).display_user_balance().display_user_balance()