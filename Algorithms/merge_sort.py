def merge_sort(list):
    """
    Sorts a list in ascending order
    return a new sorted list
    
    Devide: Find teh midpoint of the list and devide into sublists
    Conqure: Recursively sort the sublist created in previous step
    Combine: Merge the sorted sublists created in previous step
    
    O(nlogn)
    """
    
    if len(list) <=1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return (left, right)
    
def split(list):
    """
    Devide the unsorted list at midpoint into sublists
    Returns two sublist - left and right
    
    Overall run time O(logn)
    """
    
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    
    retun left, right
    
def merge(left,right):
    """
    Merge two lists(arrays), sorting them in the process
    Returns a new merged lists
    
    Overall linear time O(n)
    """
    
    l = []
    i = 0 #index of the left lists
    j = 0 #index of the right lists
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i +=1 
            
        else:
            l.append(right[j])
            j +=1
    
    while i < len(left):
        l.append(left[i])
        i +=1
        
    while j < len(right):
        l.append(right[j])
        j +=1
        
    return l
           
def verify_sorted(list):
    n = len(list)
    if n == 0 or n ==1:
        return True
    
    return list[0] < list[1] and verify_sorted([1:])
            
            
            
            
            
            
            
            
    
    
    
    
    
    