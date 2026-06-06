# 9. Recursive Neural Network Layer Cost Calculator
# Suppose the computational cost of a neural network is defined as:
# Cost(n) = Cost(n−1) + n²
# Cost(1) = 1
# Write a recursive function to calculate the total computational cost for n layers.
# Requirements:
# ● Use recursion.
# ● Return the final cost.
# ● Display the result for user-provided layer counts.

def calculate_cost(n):
    if n == 1:
        return 1

    # Recursive case
    return calculate_cost(n - 1) + n**2

layers = int(input("Enter the number of layers: "))

total_cost = calculate_cost(layers)

print("Total Computational Cost =", total_cost)