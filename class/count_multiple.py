# Count the Multiples
# Given N and a limit, count how many multiples of N exist from 1 to limit (inclusive).

n = int(input("Enter n : "))
limit = int(input("Enter limit : "))

count = 0

for i in range(1, limit + 1):
    if i % n == 0:
        count += 1

print("Count =",count)