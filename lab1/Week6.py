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
x1 = int((input("First number: ")))     
x2 = int((input("Second number: ")))   
match = 0
while x1 > 0 and x2 > 0:
    if x1 % 10 == x2 % 10:
        match += 1 
    x1 = x1 // 10
    x2 = x2 // 10
print(match) 

