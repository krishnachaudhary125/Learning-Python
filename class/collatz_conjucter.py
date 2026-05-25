# Collatz Conjecture
# Apply Collatz rule: if n is even → n//2; if odd → 3n+1. Count steps until n reaches 1.

n = int(input("Start: "))
steps = 0
while n != 1:
    print(n, end="→")
    if n % 2 == 0:
        n = n / 2
    else:
        n = n * 3 + 1
    steps += 1
print(n, " Steps:", steps)