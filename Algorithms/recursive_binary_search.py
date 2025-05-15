def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2
        
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint +1:], target) # Slice the array from midpoint to the end and search target
            else: 
                return recursive_binary_search(list[:midpoint], target) # 

def verify(result):
    print(f"Target found {result}")

arr = [x for x in range(0,10)]
target = int(input('Please enter target'))

_target = recursive_binary_search(arr, target)
verify(_target)
# Time complexity O(logn)