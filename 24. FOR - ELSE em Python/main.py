variavel = ['Denis', 'Alexandre']

for valor in variavel:
    if valor.startswith('J'):
        print('Começa com D', valor)
        break
else:
    print('Não começa com J')
