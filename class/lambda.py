# lambda vs def - same thing, different syntax
def square(): return x ** 2
sq = lambda x: x **2
print(sq(5))


# lambda with sorted() - real API use
students = [("Krishna", 3), ("Subodh", 1), ("Sumit", 2)]
ranked = sorted(students, key = lambda s: s[1], reverse = True)
print(ranked)


# lambda with map() and filter()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubled = list(map(lambda x: x * 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(doubled)
print(evens)


# lambda in ML - custom loss weight
loss_weight = lambda epoch: 1.0 / (1 + 0.1 * epoch)
print([round(loss_weight(e), 3) for e in range(5)])