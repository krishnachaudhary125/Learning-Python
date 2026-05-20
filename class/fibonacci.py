# Fibonacci — while Style
# Generate Fibonacci numbers up to a user-given limit using a while loop.

limit = int(input("Enter limit : "))
a, b = 0, 1

while a <= limit:
    print(a, end = " ")
    a, b = b, a + b