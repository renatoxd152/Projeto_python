'''Um vendedor de imóveis recebe comissão de 5% a cada imóvel vendido com o valor de até R$250.000,00 e comissão de 8% sobre imóveis vendidos que custem mais que isso. 
Faça um programa em python que leia do vendedor a quantidade de imóveis que ele vendeu. Depois, para cada imóvel vendido, leia o valor do imóvel e o tipo (se é casa, apartamento, fazenda, etc). 
Ao final seu programa deve exibir: Quanto o vendedor vendeu. Quanto o vendedor receberá de comissão. O tipo do imóvel mais caro e o seu valor. A quantidade de imóveis que custam mais que R$200.000,00 e menos que R$350.000,00. O preço médio dos imóveis. A fazenda mais barata e o seu valor. O preço médio das casas.'''
n = int(input("Quantos imóveis você vendeu ?"))
cont = 0
comissao = 0
soma = 0
maior = 0
menor = 0
qnt = 0
cont1 = 0
media_casa = 0
soma1 = 0
faz = 0
aux2 = 0

while n <= 0:
    print("Digite outro valor")
    n = int(input("Quantos imóveis você vendeu ?"))
while cont < n:
    tipo = input("Qual é o tipo do imóvel?[casa,apartamento,fazenda,etc]")
    valor = int(input("Qual o valor do imóvel?"))
    cont = cont + 1
    soma = soma + valor
    
    if cont == 1 :
        maior = menor = valor
        
    else:
        if valor > maior:
            maior = valor
            aux = tipo
            
        if tipo == "fazenda" :
            faz = faz + 1
            if valor < menor :
                menor = valor
                print(menor)
            if faz == 1:
                menor = valor
                
               
                
    if tipo == "casa":
        cont1 = cont1 + 1
        soma1 = soma1 + valor
                
    if valor <= 250000:
        porc = (valor * 5)/100
        comissao = comissao + porc
        
    else:
        porc = (valor * 8)/100
        comissao = comissao + porc
        
    if valor > 200000 and valor < 350000:
        qnt = qnt + 1
        
media_casa = soma1 / cont1
medio = soma / cont

print("O valor total que o vendendor vendeu foi:",soma)
print("A sua comissão será de:", comissao)
print("O tipo do imóvel mais caro é",aux,"e o seu valor é:",maior)
print("Quantidade de Imóveis acima de 200000 e menos que 350000:",qnt)
print("O preço médio dos imóveis é:",medio)
print("A fazenda mais barata e o seu valor:",menor)
print("O preço médio das casas é :",media_casa)




    

    
