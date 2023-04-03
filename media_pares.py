x = int(input('Quantos elementos vai ter o vetor : '))
vet = [0 for x in range(x)]
soma = 0 
y = 0 

for i in range(0,x):
    vet[i] = float(input('Digite um numero: '))
for i in range(0,x):
    if vet[i]%2 == 0:
        soma = soma + vet[i]
        y = y +1

if y == 0 :
    print('Nenhum numero par')
else: 
    media = soma /y
    print(f'Media dos pares = {media: .1f}')