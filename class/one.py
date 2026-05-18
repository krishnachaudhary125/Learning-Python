# Sum from 1 to N

n = int(input("Enter the n number : "))

total = 0

for i in range(1, n+1):
	total += i

print("Sum from 1 to ",n, "is : ", total)