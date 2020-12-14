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
"""

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
