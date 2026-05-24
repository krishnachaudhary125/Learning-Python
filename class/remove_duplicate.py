# Remove Duplicates — No set()
# Remove duplicate values from a list preserving original order. Do NOT use set() or dict.

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique = []

for n in nums:
    if n not in unique:
        unique.append(n)
print(unique)