"""
def selection_list(nums):
    n = len(nums)
    for i in range(n-1):
        mp = i
        for n in range(i+1,n):
            if nums[n] < nums[mp]:
                mp = i
        nums[i], nums[mp] = nums[mp],nums[i]
"""

def binary_search(arr, low, high, x): 
    if high >= low: 
        mid = (high + low) // 2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
        else: 
            return binary_search(arr, mid + 1, high, x) 
    else: 
        return -1
  
arr = [ 2, 3, 4, 10, 40 ] 
x = 10


result = binary_search(arr, 0, len(arr)-1, x) 
if result != -1: 
    print(str(result))
else: 
    print(-1)
