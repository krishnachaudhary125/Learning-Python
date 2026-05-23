# Inverted Star Pyramid
# Print an inverted full pyramid. Stars decrease each row, centred with spaces.

rows = int(input("Rows: "))
for i in range(rows, 0, -1):
    stars = 2 * i - 1
    spaces = rows - i
    print(" " * spaces + "*" * stars)