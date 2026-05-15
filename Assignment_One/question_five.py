# GPU Requirement Checker for Deep Learning
# Write a program that:
# Takes RAM size, GPU memory, and CUDA availability (True/False) as input.
# Uses logical operators to determine if the system can train deep learning models.
# Rules:
#   RAM ≥ 16 GB
#   GPU ≥ 6 GB
#   CUDA must be True

ram = int(input("Enter the size of RAM: "))
gpu = int(input("Enter the memory of GPU: "))
cuda = input("Enter (Y/N) if CUDA is available: ")

if cuda.lower() == "y":
    cuda_ava = True

elif cuda.lower() == "n":
    cuda_ava = False

else:
    print("Invalid input in CUDA")

if ram>=16 and gpu>=6 and cuda_ava:
    print("The system can train deep learning models")

else:
    print("The system cannot train deep learning models")