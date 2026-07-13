class Product:
	discount = 0.10
	
	def __init__(self, name, price, category = "General"):
		self.name = name
		self.price = price
		self.category = category

	def final_price(self):
  		return self.price * (1 - Product.discount)

	def __str__(self):
		return f"{self.name} - Rs.{self.final_price():.0f}"

p1 = Product("laptop", 80000, "Electronics")
p2 = Product("Pen", 20)

print(p1)
print(p2.category)