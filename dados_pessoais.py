x = int(input('Quantos alunos serao digitados: '))
vet = [0 for x in range(x)]
gen = [0 for x in range(x)]
mulher = 0 
homem = 0
soma = 0

for i in range(0,x):
    print(f'Altura da {i+1}a pessoa: ', end='')
    vet[i] = float(input(''))
    print(f'Genero da {i+1}a pessoa: ', end='')
    gen[i]= input('')
maior = vet[0]
menor = vet[0]
for i in range(1,x):
    if vet[i] > maior:
        maior = vet[i]
for i in range(1,x):
    if vet[i] < menor:
        menor = vet[i]
print(f'Menor altura = {menor}')
print(f'Maior altura = {maior}')

for i in range (0,x):
    if gen[i] == 'F':
        soma = soma + vet[i]
        mulher = mulher + 1
    else:
        homem = homem + 1
media = soma / mulher
print(f'Media das alturas das mulheres = {media:.2f}')  
print(f'Numero de homens = {homem}')


    