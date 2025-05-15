import numpy as np

"""
Find if the exist a sum of subarray that are contigious 
Return true else false 
"""
def has_subarray_with_sum(arr, target):
    curr_sum = 0 # tracks current sum
    sum_set = set([0]) # set of previous sums
    
    for num in arr:
        curr_sum += num # add old sum with current element value to find current sum
        #print(curr_sum)
        if (curr_sum - target) in sum_set: # if return num in set then sum of subarray to target exist
            return True
        sum_set.add(curr_sum) # {0, 1, 3,...} 
    return False
    
arr = [x for x in range(10)]
print(f"sum of subarray exist: {has_subarray_with_sum(arr, 10)}")