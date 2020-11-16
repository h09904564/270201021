
loop_times = int(input("How many number?: "))
even = 0
odd = 0
for i in range(loop_times):
    x = int(input("integer?: "))
    if x % 2 == 0:
        even +=1
    else:
        odd +=1
result = even / (even + odd) * 100

print(result)
