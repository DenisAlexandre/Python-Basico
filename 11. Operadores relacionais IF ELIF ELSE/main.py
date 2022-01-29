#== > >= < <= != 
num_1 = 2
num_2 = 2
expressao = (num_1 <= num_2)
print(expressao)

nome = input('Qual o seu nome: ')
idade = int(input('Qual sua idade: '))

idade_menor = 20 
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o emprestimmo. ')
else:
    print(f'{nome} não pode pegar o emprestimo')