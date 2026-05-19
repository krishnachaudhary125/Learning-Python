# Prime Checker
# Take integer N. Use nested loops or while to check if N is prime. Print Yes/No.

num = int(input("Enter number : "))

if num <= 1:
    print("Not a prime number")

else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break

    else:
        print("Prime number")