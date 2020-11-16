"""
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
"""
x1 = (input("First number: "))      #158
x2 = (input("Second number: "))     #15885
a = 0
for i in x1:
    for n in x2:
        if n == i:
            a +=1
            break

print(a)
