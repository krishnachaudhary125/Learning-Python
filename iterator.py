cars = ["BMW", "Porche", "Lamborgini", "Farrari", "Toyota"]

carit = iter(cars)

print(next(carit))
print(next(carit))
print(next(carit))
print(next(carit))
print(next(carit))

for i in cars:
    print(i)