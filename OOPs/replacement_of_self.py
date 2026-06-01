class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(hello):
    print("Hello, my name is " + hello.name)

p1 = Person("Krishna", 21)
p1.greet()