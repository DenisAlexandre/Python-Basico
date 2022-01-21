nome = "Denis"
idade = 32
altura = 1.75
e_maior = idade > 18
peso = 140
imc = (peso/ (altura ** 2))

print(f'{nome} tem {idade} anos de idade e seu imc é{imc: .2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{0} {0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc))
print('{im} tem {n} anos de idade e seu imc é {i}'.format(n=nome, i=idade, im=imc))

