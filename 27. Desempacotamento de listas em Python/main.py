lista = ['Edu', 'João', 'Luiz', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

print(lista)

n1, n2, n3, *outra_lista = lista
# *outra_lista, n1, n2, n3 = lista

print('####################')
      
print(n1, n2, outra_lista)
print(outra_lista[-1])