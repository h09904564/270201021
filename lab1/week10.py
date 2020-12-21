"""
def harmonic(num):
    if num == 1:
        return 1
    else:
        return 1/num + harmonic(num-1)

print(harmonic(500))


def reverse_my_list(liste):
    if len(liste) == 0:
        return []
    else:
        return[liste.pop()] + reverse_my_list(liste)
print(reverse_my_list([1,2,3,4]))
"""
