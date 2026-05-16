# AI Training Cost Estimator
# Create a program that:
# Takes:
#     Number of training hours
#     GPU hourly cost
#     Storage cost
# Calculates total cost.
#     Use conditions:
#     Cost > 100000 → “Enterprise Scale Training”
#     Cost > 50000 → “Mid Scale Training"

hours = int(input("Enter number of training hours : "))
gpu = float(input("Enter GPU hourly cost : "))
storage = float(input("Enter storage cost : "))

total = hours * gpu + storage

if total > 100000:
    print("Enterprise Scale Training")

elif total > 50000:
    print("Mid Scale Training")

else:
    print("Lower Scale Training")