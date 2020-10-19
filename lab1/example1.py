""""
x = 1
y = 4
z = 0.25
result = ((2*x + y)**2 * z**(1/2))/(x**(1/2) + y**(1/2))
print(result)



# q = 2*x**2 + 6*x - 20 = 0
# a*x**2 + b*x + c = 0
a = 2
b = 6
c = -20
x1 = (-b + (b**2-4*a*c)**(1/2)) / (2*a)
x2 = (-b - (b**2-4*a*c)**(1/2)) / (2*a)
print(x1,x2)
"""

temp = input("Celsius: ")
temp = float(temp)
fahrenheit = temp * 1.8 + 32
print("fahrenheir:", fahrenheit)