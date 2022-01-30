""" 
Faça um programa que peça ao usuário para digitar um  número inteiro,
informe se este número é par ou ímpar. Caso o usário nao digite um número 
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro : ')

if numero.isnumeric():
    if (numero % 2 == 0):
        print('numero par')
    else:
        print('numero impar')
        
else:
    print('O número não é inteiro')