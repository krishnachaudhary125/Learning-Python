sum = lambda x, y: x + y


#passing lambda function as an argument to another function

def average(a, sum):
    return sum/a

print(average(2, sum(5, 3)))