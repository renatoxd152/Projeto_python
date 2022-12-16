#Faça um programa que leia um número inteiro N. Após isso leia N datas no formato "dd/mm/aaaa". Seu programa deve escrever todas as datas no formato textual "dd de MMM de aaaa". Caso a data seja inválida, seu programa deve escrever "DATA INVALIDA". Utilize registro para definir a data.
class data:
  
  ano_string = ""
  dia_string = ""
  dia = 0
  mes = 0
  ano = 0

lista_datas = []

qqd_datas = int(input())
i = 0
while i < qqd_datas:
  
  data_aux = input().split("/")

  data1 = data()
  data1.dia = int(data_aux[0])
  data1.dia_string = data_aux[0]
  data1.mes = int(data_aux[1])
  data1.ano = int(data_aux[2])
  data1.ano_string = data_aux[2]
  

  lista_datas.append(data1)

  i += 1
  
for c in range(qqd_datas):
  
  validade_ano = False
  validade_dia = False
  validade = False

  if(lista_datas[c].ano > 0):
    validade_ano = True
  if(lista_datas[c].dia > 0):
    validade_dia = True
  if(lista_datas[c].mes == 1 or lista_datas[c].mes == 3 or lista_datas[c].mes == 5 or lista_datas[c].mes == 7 or lista_datas[c].mes == 8 or lista_datas[c].mes == 10 or lista_datas[c].mes == 12):
    if(lista_datas[c].dia <= 31):
      validade = True
    # Meses com 30 dias
  elif( lista_datas[c].mes == 4 or lista_datas[c].mes == 6 or lista_datas[c].mes == 9 or lista_datas[c].mes == 11):
    if(lista_datas[c].dia <= 30):
      validade = True
  elif lista_datas[c].mes == 2:
      # Testa se é bissexto
    if(lista_datas[c].ano % 4 == 0 and lista_datas[c].ano % 100 != 0) or (lista_datas[c].ano % 400 == 0):
      if(lista_datas[c].dia <= 29):
        validade = True
    elif(lista_datas[c].dia <= 28):
      validade = True

  if validade == True and validade_ano == True and validade_dia == True:
    if lista_datas[c].mes == 1:
      print(f"{lista_datas[c].dia_string} de janeiro de {lista_datas[c].ano_string}")
    elif lista_datas[c].mes == 2:
      print(f"{lista_datas[c].dia_string} de fevereiro de {lista_datas[c].ano_string}")
    elif lista_datas[c].mes == 3:
      print(f"{lista_datas[c].dia_string} de marco de {lista_datas[c].ano_string}")
    elif lista_datas[c].mes == 4:
      print(f"{lista_datas[c].dia_string} de abril de {lista_datas[c].ano_string}")
    elif lista_datas[c].mes == 5:
      print(f"{lista_datas[c].dia_string} de maio de {lista_datas[c].ano_string}")
    elif lista_datas[c].mes == 6:
      print(f"{lista_datas[c].dia_string} de junho de {lista_datas[c].ano_string}")
    elif lista_datas[c].mes == 7:
      print(f"{lista_datas[c].dia_string} de julho de {lista_datas[c].ano_string}")
    elif lista_datas[c].mes == 8:
      print(f"{lista_datas[c].dia_string} de agosto de {lista_datas[c].ano_string}")
    elif lista_datas[c].mes == 9:
      print(f"{lista_datas[c].dia_string} de setembro de {lista_datas[c].ano_string}")
    elif lista_datas[c].mes == 10:
      print(f"{lista_datas[c].dia_string} de outubro de {lista_datas[c].ano_string}")
    elif lista_datas[c].mes == 11:
      print(f"{lista_datas[c].dia_string} de novembro de {lista_datas[c].ano_string}")
    else:
      print(f"{lista_datas[c].dia_string} de dezembro de {lista_datas[c].ano_string}")
      
  else:
    print("DATA INVALIDA")
  


  
