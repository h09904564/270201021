"""
def multi(num):
    if num == 1:
        return 3
    else:
        return 3 + multi(num-1)

print(multi(5))
"""
"""
def hailstone(num):
    s = str(num)
    if num == 1:
        return s
    if num % 2 == 0:
        return s + ", " + hailstone(num//2)
    else:
        return s + ", " + hailstone ((3*num) + 1)
    
print(hailstone(10))
"""
"""
def sum_of_list(x):
    if not isinstance(x,list):
        return x
    else:
        sum = 0
        for a in x:
            sum += sum_of_list(a)
        return sum

print(sum_of_list([3,12,76,[4,56,43],[2,8],81,75]))
"""
