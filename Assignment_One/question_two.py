# AI Model Accuracy Comparator
# Write a Python program that:
# Accepts accuracy values of three ML models (float values).
# Uses comparison and logical operators to:
# Find the best model
# Check if all models exceed 90%
# Check if any model is below 70%
# Print appropriate recommendations.

modelOne = float(input("Enter first model accuracy: "))
modelTwo = float(input("Enter second model accuracy: "))
modelThree = float(input("Enter third model accuracy: "))

if modelOne>90 and modelTwo>90 and modelThree>90:
    print("You can use any of those AI Model")

elif modelOne<70 and modelTwo<70 and modelThree<70:
    print("Non of them are recommended")

else:
    if modelOne>modelTwo:
        if modelOne>modelThree:
            print("Model one is recommended")
        else:
            print("Model three is recommended")

    else:
        if modelTwo>modelThree:
            print("Model two is recommended")
        else:
            print("Model three is recommended")

