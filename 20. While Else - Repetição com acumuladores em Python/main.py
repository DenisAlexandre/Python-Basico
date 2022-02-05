contador = 0
acumualdor = 0
while contador <= 5:
    print(contador, acumualdor)
    
    if contador > 5:
        break
    
    contador += 1
    acumualdor += contador
    
else: 
    print('Cheguei no else.')
print('Iso será executado')