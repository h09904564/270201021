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
"""
def get_evens(l):
    return _get_evens_recursive(l, 0)
def _get_evens_recursive(l, c=0):
    if len(l) == 0:
        return c
    current = l.pop()
    if current >= 0 and current %2 == 0:
        c +=1
    return _get_evens_recursive(l,c)
"""
