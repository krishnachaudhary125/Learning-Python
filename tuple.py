fruit = ("apple", "banana", "cherry")
print(fruit)

single_tuple = ("apple",)
print(single_tuple)

print(len(fruit))

print(type(fruit))

#Changing tuple value

fruit_list = list(fruit)  #tuple to list
fruit_list.append("orange")
fruit_tuple = tuple(fruit_list)  #list to tuple
print(fruit_tuple)