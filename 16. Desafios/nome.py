""" 
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite o seu nome: ')
tam =len(nome)
if(tam <= 4):
    print('nome curto')
elif(tam <= 6):
    print('normal')
else:
    print('muito grande')