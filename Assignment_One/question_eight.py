# Bank Loan Eligibility for Startup Founders
# Write a program for startup founders seeking investment:
# Input:
#     Monthly income
#     Credit score
#     Existing debt
# Conditions:
#     Income > 100000 AND credit score > 750 AND debt < 50000
#     Eligible for “Premium Loan”
# Add additional eligibility levels using elif.

income = float(input("Enter monthly income : "))
score = float(input("Enter credit score : "))
debt = float(input("Enter existing debt : "))

if income > 100000 and score > 750 and debt < 50000:
    print("Premium loan")

elif income > 50000 and score > 300 and debt < 10000:
    print("Regular loan")

else:
    print("Not eligible for loan")