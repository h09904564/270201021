"""
my_tuple = [("Jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44), ("Bran",10)]

for a,b in my_tuple:
    if b > 18:
        print(a)
"""


m_dict={}
books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
for n in books:
    count = 0
    liste = []
    for i in n:
        count +=1
        if i not in liste:
            liste.append(i)
        else:
            pass

    m_dict[n] = (count,len(liste))

print(m_dict)
