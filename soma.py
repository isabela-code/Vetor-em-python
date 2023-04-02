x = int(input('Quantos numeros voce vai digitar? '))
vet1 = [0 for x in range(x)]
vet2 = [0 for x in range(x)]

print('Digite os valores do vetor de A:')
for i in range (0,x):
    vet1[i] = int(input(''))
print('Digite os valores do vetor de B:')
for i in range (0,x):
    vet2[i]= int(input(''))

print('Vetor resultante: ')

for i in range(0,x):
    soma = vet1[i]+vet2[i]
    print(f'{soma}')

