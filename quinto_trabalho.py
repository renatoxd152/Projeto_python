'''
Melhor investimento[1]:

Um banco oferece a seus clientes 3 formas de investimentos: Poupança, LCI e CDB. Faça um programa que receba de entrada um número real, representando o valor que o cliente deseja investir, e um número inteiro, representando a quantidade de meses que o cliente pretende deixar o dinheiro no investimento. Seu programa deve escrever na tela o valor que o cliente terá ao término do período de investimento em cada produto oferecido pelo banco. Em seguida escreva na tela a primeira letra do melhor produto de investimento para o valor e tempo escolhidos pelo cliente, em maiúscula (Verifique na seção “Exemplos de Entrada e Saída" o formato correto que o seu programa deve imprimir).

Considere as seguintes rentabilidades para cada produto:

Poupança: juros de 0.59% ao mês;
LCI: juros de 0.86% ao mês;
CDB: juros de 1.032% ao mês.
Considere ainda as seguintes situações:

A Poupança e a LCI são isentas de imposto de renda;
A LCI tem um prazo mínimo de investimento de 6 meses. Assim, considere sua rentabilidade igual a 0% se o prazo apresentado pelo cliente for menor do que 6 meses;
A rentabilidade de um investimento em CDB é tributada pela Receita Federal. O valor real que o cliente irá receber será Valor_investido + Rentabilidade – (Imposto * Rentabilidade). Você deve deduzir o valor do imposto a ser pago para apresentar o valor real que o cliente terá disponível, caso escolha este tipo de investimento. A tributação é determinada pelo tempo de investimento, nos seguintes valores:
o de 1 a 6 meses: 22,5%;
o de 7 a 12 meses: 20%;
o de 13 a 24 meses: 17,5%;
o acima de 24 meses: 15%;
Escreva os valores de cada investimento na ordem Poupança, LCI e CDB, com um valor por linha e com 2 casas decimais.
'''
def poupanca(investir, meses):
#POUPANCA
    if meses == 1:
        resultado1 = investir + (investir * 0.59) / 100
        return resultado1
    else:
        for x in range(1, meses):
            investir = investir + (investir * 0.59) / 100
            for d in range(x):
                resultado1 = investir + (investir * 0.59) / 100
        return resultado1

def lci(investir, meses):
#LCI
    if meses >= 6:
        rentabilidade = 0.86
        for i in range(1, meses):
            investir = investir + (investir * rentabilidade) / 100
            for j in range(i):
                resultado2 = investir + (investir * rentabilidade) / 100
    else:
        resultado2 = investir
    return resultado2

def cdb(investir, meses):
    
    aux = investir
    #CDB
    if meses >= 1 and meses <= 6:
        imposto = 22.5
    elif meses >= 7 and meses <= 12:
        imposto = 20.0
    elif meses >= 13 and meses <= 24:
        imposto = 17.5
    else:
        imposto = 15
    if meses == 1:
        acumulado = investir + (investir * 1.032) / 100
        rentabilidade2 = acumulado - investir
        resultado3 = investir + rentabilidade2 - ((22.5 * rentabilidade2)/100)
        return resultado3
    else:
        for y in range(1, meses):
            investir = investir + (investir * 1.032) / 100
            for r in range(y):
                auxiliar = investir + (investir * 1.032) / 100
                c = auxiliar
        rentabilidade1 = c - aux
        resultado3 = aux + rentabilidade1 - ((imposto*rentabilidade1)/100)
        return resultado3
        
entrada = input().split()
investir = float(entrada[0])
meses = int(entrada[1])

resultado_poupanca = poupanca(investir, meses)
resultado_lic = lci(investir, meses)
resultado_cdb = cdb(investir, meses)

print("{:.2f}".format(resultado_poupanca))
print("{:.2f}".format(resultado_lic))
print("{:.2f}".format(resultado_cdb))

if resultado_poupanca > resultado_lic and resultado_poupanca > resultado_cdb:
    print("P")
elif resultado_lic > resultado_cdb:
    print("L")
else:
    print("C")
    
