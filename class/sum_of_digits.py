# Sum of Digits
# Take an integer input. Find the sum of all its individual digits

num = input("Enter number : ")

sum = 0

for digit in num:
    sum += int(digit)

print("Sum of digits",num,"=",sum)