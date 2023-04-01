x = int(input('Quantos numeros voce vai digitar : '))
vet = [0 for x in range(x)]
soma = 0 

for i in range (0,x):
    vet[i] = int(input('Digite um numero: '))

print(f'Valores = ',end='')
for i in range (0,x):
    print(f'{vet[i] : .1f}', end='')
print()

for i in range (0,x):
    soma = soma + vet[i]
    media = soma / x
print(f'Soma = {soma}')
print(f'Media = {media}')
    