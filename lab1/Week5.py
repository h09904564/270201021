"""
number = int(input("Enter a number: "))
if number>=10:
   ones = number % 10 
   tens = (number//10) % 10
   result = ones + tens
else:
    result = number

print(result)
"""
year = int(input("What year are you in?: "))

if year % 4 ==0:
    print("You are in a leap year!!!")
else:
    print("You are in a century year.")
