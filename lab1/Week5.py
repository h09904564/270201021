"""
number = int(input("Enter a number: "))
if number>=10:
   ones = number % 10 
   tens = (number//10) % 10
   result = ones + tens
else:
    result = number

print(result)

nums = [8,60,43,55,25,134,1]
a = 0
for i in nums:
   a = a + i 
print(a)


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result = 1
if b > 0:
    for i in range(0,b,1):
        result = a * result
elif b == 0:
    result = 1
else:
    for i in range(0,b,-1):
        result = result / a
print(result)
"""

facto = int(input("Enter me a number: "))
result = 1
for i in range(1,facto+1):
    result = i * result
print(result)
