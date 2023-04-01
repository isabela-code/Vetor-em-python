x = int(input('Quantas pessoas serão digitadas :'))
vet = [0 for x in range(x)]
ida = [0 for x in range(x)]
alt = [0 for x in range(x)]
soma = 0
soma2 = 0 

for i in range(0,x):
    print(f'Dados da {i+1}a pessoa :')
    vet[i] = input('Nome :')
    ida[i] = int(input('Idade:'))
    alt[i] = float(input('Altura:'))
print()

for i in range(0,x):
    soma = soma + alt[i]
    media = soma/x
print(f'Altura media : {media : .2f}')

for i in range(0,x):
    if ida[i] < 16:
        soma2 = soma2 + 1
        porcento = (soma2 * 100)/x
print(f'Pessoas com menos de 16 anos : {porcento : .1f}%')
for i in range(0,x):
    if ida[i]<16:
        print(f'{vet[i]:{x}}')
