# Checkerboard Grid
# Print an N×N checkerboard using # and spaces. Alternate based on row+col parity.

n = int(input("Size: "))
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()
