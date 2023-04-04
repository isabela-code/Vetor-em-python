x = int(input('Quantos produtos serão digitados: '))
vet = [0 for x in range(x)]
compra = [0 for x in range(x)]
venda = [0 for x in range(x)]
abaixo = 0 
media = 0 
acima = 0 
comprat = 0
vendat = 0

for i in range(0,x):
    print(f'Produto {i+1}:')
    vet[i] = input('Nome : ')
    compra[i]= float(input('Preço de compra: '))
    venda[i]= float(input('Preço de venda: '))
for i in range (0,x):
    lucro = ((venda[i]*100)/compra[i]) - 100
    if lucro < 10:
        abaixo = abaixo + 1
    elif lucro >= 10 and lucro <= 20:
        media = media + 1
    else :
        acima = acima + 1
    comprat = comprat + compra[i]
    vendat = vendat + venda[i]
total = vendat - comprat
print()
print('RELATORIO')
print(f'Lucro abaixo de 10% : {abaixo}')
print(f'Lucro entre 10% e 20% : {media}')
print(f'Lucro acima de 20% : {acima}')
print(f'Valor total de compras : {comprat:.2f}')
print(f'Valor total de vendas : {vendat:.2f}')
print(f'Lucro total : {total:.2f}')
    
