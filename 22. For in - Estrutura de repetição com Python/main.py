texto = 'Python'

for letra in texto:
    print(letra)

print("####################")
for n, letra in enumerate(texto):
    print(n, letra)
    
print("####################")
for numero in range(20, -10, -3):
    print(numero)
    
print("####################")
for n in range(100):
    if n % 8 == 0:
        print(n)