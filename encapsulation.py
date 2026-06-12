class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited Rs.{amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn Rs.{amount}")
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


account = BankAccount("Krishna", 5000)

account.deposit(2000)
account.withdraw(1000)

print("Current Balance:", account.get_balance())