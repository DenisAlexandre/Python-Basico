"""
Faça um programa que pergunte a hora ao usuário e, basenado-se no horario
descrito, exiba a saudação apropriada. Ex,
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
 
horario = input('Digite o horario: ')
hora, minutos = horario.split(':')
hora = int(hora)
if (hora < 0 or hora > 23):
    print('horário invalido')
else:
    if(hora <= 11):
        print('bom dia')
    elif(hora <= 17):
        print('boa tarde')
    else:
        print('boa noite')
