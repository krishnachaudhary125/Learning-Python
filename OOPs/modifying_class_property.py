class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Krishna")
p2 = Person("Subodh")

Person.lastname = "Chaudhary"

print(p1.lastname)
print(p2.lastname)