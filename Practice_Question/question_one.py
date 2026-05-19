# Sum 1 to N
# Take integer N from user. Use a for loop to calculate 1+2+...+N. Print the sum.

n = int(input("Enter a number : "))
total = 0

for i in range(1, n+1):
    total += i

print("Sum of number from 1 to",n," is :",total)