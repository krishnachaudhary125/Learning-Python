base = input("Enter base : ")
base = int(base)
height = input("Enter height : ")
height = int(height)
area = base * height
print("Area of triangle = ", area)

if area >= 25:
    print("Area is greater than 25")
else:
    print("Area is smaller than 25")