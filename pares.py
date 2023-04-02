x = int(input('Quantos numeros voce vai digitar? '))
vet = [0 for x in range(x)]
pares = 0 

for i in range (0,x):
    vet[i] = int(input('Digite um numero: '))
print('Numeros pares :')
for i in range (0,x):
    if vet[i]%2 == 0:
        pares = pares + 1
        print(f'{vet[i]:{x}}',end='')
print()

print(f'Quantidades de pares = {pares}')