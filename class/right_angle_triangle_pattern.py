# Right-Angle Triangle Pattern
# Print a right-angle triangle of stars for a given number of rows.

rows = int(input("Rows: "))
for i in range(1, rows + 1):
    print("*" * i)
