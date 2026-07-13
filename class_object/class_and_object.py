class Student:
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def grade(self):
		return "A" if self.score >= 90 else "B"

s1 = Student("Alice", 95)
s2 = Student("Bob", 78)

print(s1.name, s1.grade())
print(s2.name, s2.grade())
print(type(s1))