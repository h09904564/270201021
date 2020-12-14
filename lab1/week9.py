"""
def function(a_list):
    summ = 0
    for i in a_list:
        summ += i
    return (summ * summ)

a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
result = function(a_list)
print(result)


def is_prime(integer):
    prime = True
    for i in range(2,integer):
        if integer % i == 0:
            prime = False
    if prime == True:
        return integer

print(is_prime(10))


import random
def random_list(b=0,e=10,N=5):
    return random.sample(range(b, e), N)
def main():
    x1 = random_list()
    x2 = random_list()


    new_list = []
    for i in x1:
        for n in x2:
            if n == i:
                new_list.append(n)
    return new_list

print(main())
"""
"""
def binary_to_dec(binary):
    binary = str(binary)
    x = 0
    a = 0
    for i in binary[::-1]:
        i = int(i)
        i = i * (2**x)
        x += 1
        a +=i
    return(a,x)

print(binary_to_dec(10010))
"""

def password_checker(user_password):
    special_cha=["-","+","*"]
    user_password = str(user_password)
    a=0
    b=0
    c=0
    if len(user_password) < 8:
        return "level 0"
    if " " in user_password:
        return "level 0"
    for i in user_password:
        if i.isalpha():
            a = 1
        elif i.isnumeric():
            b = 1
        else:
            c = 1
    return a + b + c
print(password_checker("abc12--***+ds3"))
