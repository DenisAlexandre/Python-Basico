lista = [
    #0      1       2    
    ['Edu', 'João', 'Luiz'],     # 0
    ['Maria', 'Aline', 'Joana'], # 1
    ['Helena', 'Ed', 'Lu']       # 2
]

print(lista)
print(lista[1])
print(lista[1][2])

enumerada = list(enumerate(lista))
print(list(enumerada))

for v1, v2 in enumerate(lista, 53):
    print(v1, v2)