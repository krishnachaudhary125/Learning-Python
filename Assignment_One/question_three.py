# Dataset Validation Checker
# Create a program that:
# Takes total rows, missing rows, and duplicate rows from user input.
# Calculates clean data percentage using arithmetic operators.
# Uses conditionals:
#   ≥ 95% clean → “Production Ready”
#   80–94% → “Needs Cleaning”
#   Below 80% → “Poor Dataset”
# Use explicit type casting for calculations.


total_rows = int(input("Enter number of total rows: "))
missing_rows = int(input("Enter number of missing rows: "))
duplicate_rows = int(input("Enter number of duplicate rows: "))

percentage = 100 - (((float(missing_rows) + float(duplicate_rows))*100)/float(total_rows))

if percentage>=95:
    print("Production ready")

elif percentage>=80 and percentage<=94:
    print("Needs cleaning")

else:
    print("Poor dataset")