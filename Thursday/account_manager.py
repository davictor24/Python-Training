class Account:
    def __init__(self, account_name, account_number, initial_amount):
        self.account_name = account_name
        self.account_number = account_number
        self._balance = initial_amount

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        password = input("Enter password: ")
        if password == "MyPassword":
            self._balance = value
            print("Password is correct. Account balance set.")
        else:
            print("Password is incorrect!")
        

myaccount = Account("John", "00206", 5000)

print(myaccount.account_name)
print(myaccount.account_number)
print(myaccount.balance)


print("\nChanging account balance...")
myaccount.balance = 100000

print(myaccount.balance)

