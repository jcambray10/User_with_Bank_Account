class User:
    def __init__(self, username, email_address, rate, balance):
        self.name = username
        self.email = email_address
        self.int_rate = (rate * 0.0)
        self.balance = balance
        self.amount = 0
        # other methods

    def make_deposit(self, amount):
        self.balance += amount	# hmmm...the User class doesn't have an account_balance attribute anymore
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")

    def yield_interest(self):
        if self.balance < 0:
            interest_yielded = self.balance * self.int_rate
            self.balance += interest_yielded
            return self

FCBarcelona = User("FCB", "FCB@python.com", 0, 100)

FCBarcelona.make_deposit(100).make_withdrawal(50).display_user_balance()

# python User_with_Bank_Accounts.py 

# echo "# User_with_Bank_Account" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/jcambray10/User_with_Bank_Account.git
# git push -u origin main