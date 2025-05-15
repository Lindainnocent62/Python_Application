# Linear search and validate index_found

"""
    promp user for target value
    search and return index if target exist else None
    validate index and return the index in which target was found
"""

# Search for target
def linear_search(arr, target):
    for i in range(0, len(arr)):
        print(i)
        if i == target:
            return i
    return None
    
# Validate index
def validate(i):
    if i is not None:
        print(f"Target found at index: {i}")
    else:
        print(f"Target not found")

arr = [x for x in range(0 , 10)]

target = int(input('Please enter target to search'))
index_found= linear_search(arr, target)
validate(index_found)