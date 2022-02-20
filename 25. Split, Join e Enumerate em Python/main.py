string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista1  = string.split(' ')
lista2 = string.split(',')

print(lista1)
print(lista2)

for valor in lista1:
    print(f'A palavra {valor} apareceu {lista1.count(valor)} x na frase.')
    
for valor in lista2:
    #strip: remova os espaços no início e no final da string:
    #capitalize: método retorna uma string onde o primeiro caractere é maiúsculo e o restante é minúsculo.
    print(valor.strip().capitalize())
    
string  = 'O Brasil é penta.'
lista = string.split(' ')
string2 =  ','.join(lista)


print(lista)
print(string2)

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])
    
    
lista = [
    [1, 2],
    [3, 4],
    [5, 6],
]

print("##########")

for v in lista:
    print(v[0], v[1])
    
n1, n2, n3 = lista
print(n1)