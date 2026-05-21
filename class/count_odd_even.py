# Count Evens & Odds
# Given a list of integers, count how many are even and how many are odd using a single for loop.

nums = [4, 7, 2, 9, 10, 3, 15, 8]
even_count = 0
odd_count = 0
for n in nums:
    if n % 2 == 0:
        even_count += 1
else:
    odd_count += 1
print("Evens:", even_count)
print("Odds: ", odd_count)
