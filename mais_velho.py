x = int(input('Quantos elementos vai ter o vetor : '))
vet = [0 for x in range(x)]
ida = [0 for x in range(x)]
y = 0

for i in range(0,x):
    print(f'Dados da {i+1}a pessoa')
    vet[i] = input('Nome : ')
    ida[i] = int(input('Idade :'))
maior = ida[0]
for i in range(1,x):
    if ida[i] > maior:
        maior = ida[i]
        y = i
print(f'Pessoa mais velha : {vet[y]}')
