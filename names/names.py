import time
import os
import sys
from binary_search_tree import BinarySearchTree

start_time = time.time()

with open(os.path.join(sys.path[0], 'names_1.txt'), 'r') as f:
    names_1 = f.read().split("\n")  # List containing 10000 names

# Uncomment below to use the bst:
'''
bst = BinarySearchTree('Heather')
for name in names_1:
    bst.insert(name)
'''

with open(os.path.join(sys.path[0], 'names_2.txt'), 'r') as f:
    names_2 = f.read().split("\n")  # List containing 10000 names

duplicates = []  # Return the list of duplicates in this data structure


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low + high)//2
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1
    return -1


# This implementation doesn't use the bst
#  0.08800506591796875 seconds
names_1.sort()
for name in names_2:
    if binary_search(names_1, name) != -1:
        duplicates.append(name)


# This is the original implementation:
# About 10 seconds
'''
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''

# This implementation uses the bst:
# 0.13100862503051758 seconds
'''
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)
'''

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
