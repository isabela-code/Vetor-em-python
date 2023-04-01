x = int(input('Quantos numeros voce vai digitar : '))
vet = [0 for x in range(x)]

for i in range (0,x):
    vet[i] = int(input('Digite um numero: '))

for i in range (0,x):
    if vet[i] < 0:
        print('Numeros negativos :')
        print(f'{vet[i]:{x}}')