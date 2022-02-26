"""
0 10
1 9
2 8
3 7
4 6 
5 5
6 4
7 3 
8 2
"""

for p, r in enumerate(range(10, 1, -1)):
    print(f'{p} {r}')

i = 0 
j = 10
parada = False

while not parada:
    print(f'{i} {j}')
    if(i == 8 or j == 2):
        parada = True
    i += 1
    j -= 1    

    