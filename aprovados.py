x = int(input('Quantos alunos serao digitados: '))
vet = [0 for x in range(x)]
nota1 = [0 for x in range(x)]
nota2 = [0 for x in range(x)]
y = 0

for i in range(0,x):
    print(f'Digite nome, primeira e segunda nota do {i+1} aluno:')
    vet[i]=input('')
    nota1[i]= float(input(''))
    nota2[i]= float(input(''))
print('Alunos aprovados: ')
for i in range(0,x):
    soma = nota1[i]+nota2[i]
    media = soma/2
    if media >= 6:
        print(f'{vet[y]}')
    y = y +1

