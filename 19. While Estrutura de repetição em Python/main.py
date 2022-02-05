x = 0 
while x <= 5:
    print(f'{x}')
    x+= 1
print("FIM 01")

x = 0
while x <= 5:
    if( x == 3):
        x += 1
        continue
    print(f'{x}')
    x+= 1
print("FIM 02")

x = 0
while x <= 5:
    if( x == 3):
        x += 1
        break
    print(f'{x}')
    x += 1
print("FIM 03")

x = 0 #coluna x: 0 
while x < 10:
    y = 0 #linha y: 0    
    while y < 5:
        print(f'({x}, {y})')
        y+= 1
    x += 1
    
print("FIM 04")

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite um número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]sim ou [n]ão: ')
    
    if sair == 's':
        break
    
    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Você precisa digitar um número.")
        continue
    
    num_1 = int(num_1)
    num_2 = int(num_2)
    
    # +-/*
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 *  num_2)
    elif operador == '/':
        print(num_1 /  num_2)
    else: 
        print("Erro")
