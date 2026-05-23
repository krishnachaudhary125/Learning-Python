# Find Second Largest
# Without using sort() or max(), find the second largest element in a list using loops only.

nums = [12, 45, 7, 89, 23, 56, 34]
first = float('-inf')
second = float('-inf')
for n in nums:
    if n > first:
        second = first
        first = n
    elif n > second and n != first:
        second = n

print("Second Largest:", second)