class User:
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account_balance = account_balance
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)
    def transfer_money_to_rykard(self, amount):
        self.account_balance -= amount
        rykard.account_balance += amount

margit = User("margit", "margit@fellomen.ring", 400)
rennala = User("rennala", "rennala@respec", 1000)
rykard = User("rykard", "rykard@bigyucky", 0)

margit.make_deposit(100)
margit.make_deposit(50)
margit.make_deposit(125)
margit.make_withdrawal(125)
margit.display_user_balance()

rennala.make_deposit(300)
rennala.make_deposit(200)
rennala.make_withdrawal(700)
rennala.make_withdrawal(2)
rennala.display_user_balance()

rykard.make_deposit(10)
rykard.make_withdrawal(2)
rykard.make_withdrawal(3)
rykard.make_withdrawal(1)
rykard.display_user_balance()

margit.transfer_money_to_rykard(90)
margit.display_user_balance()
rykard.display_user_balance()