x = int(input('Quantos numeros voce vai digitar? '))
vet = [0 for x in range(x)]

for i in range (0,x):
    vet[i] = int(input('Digite um numero: '))
maior = vet[0]
for i in range(1,x):
    if vet[i] > maior:
        maior = vet[i]
        posicao = i
print(f'Maior valor = {maior}')
print(f'Posição do maior valor = {posicao}')