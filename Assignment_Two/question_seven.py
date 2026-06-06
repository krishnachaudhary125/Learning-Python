# 7. Recursive Dataset Folder Scanner
# A dataset is organized in nested folders:
# dataset = {
# "train": {
# "cats": 500,
# "dogs": 450
# },
# "test": {
# "cats": 120,
# "dogs": 130
# }
# }
# Write a recursive function that traverses the nested dictionary and calculates the total number of
# images.
# Requirements:
# ● Use recursion.
# ● Function must work for any nesting level.
# ● Return the total image count.

dataset = {
    "train": {
        "cats": 500,
        "dogs": 450
    },
    "test": {
        "cats": 120,
        "dogs": 130
    }
}

def count_images(data):
    total = 0

    for value in data.values():
        if isinstance(value, dict):
            total += count_images(value)
        else:
            total += value

    return total

total_images = count_images(dataset)

print("Total Images:", total_images)