# FizzBuzz
# Print 1–50. For multiples of 3 print Fizz, multiples of 5 print Buzz, both → FizzBuzz.

num = 50

for i in range (1, num+1):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0 and i % 5 != 0:
        print("Fizz")

    elif i % 3 != 0 and i % 5 == 0:
        print("Buzz")

    else:
        print(i)
        i+=1

