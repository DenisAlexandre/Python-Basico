"""
Formatando valores com modificadores 

:s - Texto (strings)
:d - Inteiros (int)
:f - String
:. (Número) f Quantidade de casas decimais (float)
: (CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
num_1 = 10
print(f'{num_1:0>10}')
print(f'{num_1:1<10}')
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome = "Denis Alexandre"
#print(50 - len(nome))
print(f'{nome:#^50}')

nome_formatado = '{:@>50}'.format(nome) 
print(nome_formatado)

nome = "Denis"
sobrenome = "Alexandre"
nome_formatado = '{0:$^50} {1:#^50}'.format(nome, sobrenome)
print(nome_formatado)

print(nome.lower())
print(nome.upper())
print(nome.title())

nome = nome.ljust(20, "#")
sobrenome = sobrenome.rjust(20, '#')
print(nome)
print(sobrenome)
