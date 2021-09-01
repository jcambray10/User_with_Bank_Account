class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate 
        self.balance = balance 
        
    def deposit(self, amount):
        self.balance += amount 
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount 
        else:
            self.balance -= 5 
            print("Insufficient Funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        return self

class User:
    def __init__(self, name, email, int_rate=0, balance=0):
        self.name = name
        self.email = email
        self.account=BankAccount(int_rate, balance)

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