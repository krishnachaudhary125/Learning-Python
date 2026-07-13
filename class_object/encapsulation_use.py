class BankAccount:
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance
		self.__balance = balance

	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount
	
	def get_balance(self):
		return self.__balance

	def __str__(self):
		return f"{self.owner}: Rs.{self.__balance}"

acc = BankAccount("Alice", 5000000)
acc.deposit(100000)
print(acc.get_balance())
print(acc.owner)
print(acc._BankAccount__balance)