name = "Krishna"

def name_one():
    print("My name is " + name)

def name_two():
    name = "Subodh"
    print("My name is " + name)

def name_three():
    global name_frn
    name_frn = "Sumit"
    print("My name is " + name_frn)

name_one()
name_two() 
name_three()

print("My name is " + name_frn)