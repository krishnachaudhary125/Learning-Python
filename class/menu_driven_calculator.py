# Menu-Driven Calculator
# Build a calculator with menu: 1=Add, 2=Sub, 3=Mul, 4=Div, 5=Exit. Loop until 5.

while True:
    print("1.Add 2.Sub 3.Mul 4.Div 5.Exit")
    choice = int(input("Choice: "))

    if choice == 5:
        break

    a = float(input("A: "))
    b = float(input("B: "))

    if choice == 1:
        print(a + b)
    elif choice == 2:
        print(a - b)
    elif choice == 3:
        print(a * b)
    elif choice == 4:
        if b != 0:
            print(a / b)
        else:
            print("Div by 0!")