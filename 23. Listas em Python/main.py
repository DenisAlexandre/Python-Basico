#         0    1    2    3    4   5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(lista[0:3])
print(lista[2:])
print(lista[-1])
print(lista[::-1])

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend('a')
l2.extend('b')
l2.insert(0, 'Denis')
l2.pop()
del(l2[0:1])
l3 = l1 + l2 

print(l1)
print(l2)
print(l3)
print(l2[0])

print(max(l2))
print(min(l2))

l4 = list(range(0, 100, 7))
print(l4)

for valor in l2:
    print(valor)


