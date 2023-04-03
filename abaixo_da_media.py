x = int(input('Quantos elementos vai ter o vetor : '))
vet = [0 for x in range(x)]
soma = 0 

for i in range(0,x):
    vet[i] = float(input('Digite um numero: '))
    soma = soma + vet[i]
media = soma/x
print(f'Media do vetor = {media: .3f}')
print('Elementos abaixo da media: ')
for i in range (0,x):
    if vet[i] < media:
        print(f'{vet[i]}')