# Binary search and validate index_found

"""
    promp user for target value
    search and return index if target exist else None
    validate index and return the index in which target was found
"""

# Search for target
def binary_search(arr, target):
    first = 0
    last = len(arr)-1 # Constant run time

    while first <= last:
        midpoint = (first + last)//2 # Floor division i.e round to the lowest factor
        
        if arr[midpoint] == target: 
            return midpoint
        elif arr[midpoint] < target:
            first = midpoint + 1
        else: 
            last = midpoint -1
    return None
    
# Validate index
def validate(i):
    if i is not None:
        print(f"Target found at index: {i}")
    else:
        print(f"Target not found")

arr = [x for x in range(0 , 10)]

target = int(input('Please enter target to search'))
index_found= binary_search(arr, target)
validate(index_found)
# The time complexity is O(logn)