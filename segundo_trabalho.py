'''Faça um programa que gerencie veículos e clientes de uma locadora de carros, de acordo com os seguintes requisitos: O sistema deve possuir um menu interativo O sistema deve permitir o cadastro de veículos e clientes com os seguintes dados: Veículo: código, modelo (nome) e ano de fabricação Cliente: cpf, nome, ano de nascimento O sistema deve permitir a listagem de veículos e clientes O sistema deve permitir a busca por veículos e clientes, por meio do código e cpf respectivamente O sistema deve permitir a remoção de veículos e cliente, por meio do código e cpf respectivamente O sistema deve possuir um submenu de geração de relatório que contenham opção para: Exibir qual o modelo de carro que mais existe na locadora. Exibir todos os modelos de carros juntamente com a quantidade de cada um na locadora Exibir as informações do carro mais velho Se houver mais de um, imprimir todos Exibir as informações do carro mais novo Se houver mais de um, imprimir todos Exibir a quantidade e a porcentagem de clientes jovens (entre 18 e 23 anos), adultos (entre 24 e 69 anos) e idosos (acima de 70 anos) Exibir a porcentagem de carros da locadora que não são obrigados a pagar IPVA no estado de SP (carros mais velhos que 20 anos) O sistema deve tratar alguns erros e mostrar mensagens de alerta, por exemplo: Ao tentar remover, listar ou pesquisa veículos e/ou clientes quando não há nada cadastrado Ao tentar remover veículos que o id não existe Ao escolher uma opção inválida no menu Ao tentar inserir veículos com mesmo código e clientes com mesmo cpf'''
from datetime import datetime
now = datetime.now()

#-----------------------------------------------       
#Def para definir a idade do carro
def ipva(veiculos_ano):
  idade = 0
  cont = 0
  atual = now.year
  resultado = 0
  for i in range(len(veiculos_ano)):
    idade = atual - veiculos_ano[i]
    idade = int(idade)
    if idade >= 20:
      cont = cont + 1

  if cont != 0:      
    resultado = cont / len(veiculos_ano) *100
  else:
    print('Não há veiculos que não pagam IPVA')
  
  print("A porcentagem de carros da locadora que não são obrigados a pagar IPVA no estado de SP é:",resultado,"%")

#-----------------------------------------------
#Def para definir a idade real das pessoas
def pessoas(ano_nascimento):
  porc1 = 0
  porc2 = 0
  porc3 = 0  
  cont1 = 0
  cont2 = 0
  cont3 = 0
  atual = now.year
  
  for i in range(len(ano_nascimento)):
    idade = atual - ano_nascimento[i]
    idade = int(idade)
    if idade >= 18 and idade <= 23:
      cont1 = cont1 + 1
    elif idade >= 24 and idade <= 69:
      cont2 = cont2 + 1
    elif idade >= 70:
      cont3 = cont3 + 1

  porc1 = cont1 / len(ano_nascimento) * 100
  porc2 = cont2 / len(ano_nascimento) * 100
  porc3 = cont3 / len(ano_nascimento) * 100

  print("A quantidade de clientes jovens é:",cont1,",e a porcentagem é:",porc1,"%")
  print("A quantidade de clientes adultos é:",cont2,",e a porcentagem é:",porc2,"%")
  print("A quantidade de clientes idosos é:",cont3,",e a porcentagem é:",porc3,"%") 
#-----------------------------------------------
def carro_novo(veiculos_ano ,veiculos_codigo, veiculos_modelo):
  novo = 0
  menor = 0
  atual = now.year
  idade = 0
  
  for i in range(len(veiculos_ano)):
    idade = atual - veiculos_ano[i]
    if i == 0:
      menor= veiculos_ano[i]
    if idade <= menor:
      menor = idade
      novo = veiculos_ano[i]
  
  for i in range(len(veiculos_ano)):
    if novo == veiculos_ano[i]:
      v_codigo = veiculos_codigo[i]
      v_modelo = veiculos_modelo[i]
      v_ano = veiculos_ano[i]
      print("\nVeiculo codigo: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano))       

#-----------------------------------------------
def carro_velho(veiculos_ano ,veiculos_codigo, veiculos_modelo):
  
  velho = 0
  maior = 0
  atual = now.year
  idade = 0
  
  for i in range(len(veiculos_ano)):
    idade = atual - veiculos_ano[i]
    if i == 0:
      maior = veiculos_ano[i]
    if idade >= maior:
      maior = idade
      velho = veiculos_ano[i]
  
  for i in range(len(veiculos_ano)):
    if velho == veiculos_ano[i]:
      v_codigo = veiculos_codigo[i]
      v_modelo = veiculos_modelo[i]
      v_ano = veiculos_ano[i]
      print("\nVeiculo codigo: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano))       
      
#-----------------------------------------------
def quantidade_modelo(veiculos_modelo):
  cont = 0
  posicao = 0

  for i in range(len(veiculos_modelo)):
    posicao = veiculos_modelo[i]

    for i in range (len(veiculos_modelo)):
      if posicao == veiculos_modelo[i]:
        cont = cont + 1
            
    print('O modelo ',posicao,'possui ',cont,'veiculos.')  
    cont = 0
    
#Exibir todos os modelos de carros juntamente com a quantidade de cada um na locadora    
      
#-----------------------------------------------
#Exibir qual o modelo de carro que mais existe na locadora.
def modelo_frequente(veiculos_modelo):
  posicao = 0
  modelo = 0
  maior = 0
  cont = 0
  
  for i in range(len(veiculos_modelo)):
    posicao = veiculos_modelo[i]
    
    for i in range (len(veiculos_modelo)):
     if posicao == veiculos_modelo[i]:
       cont = cont + 1
    
    if cont > maior:
      maior = cont
      modelo = veiculos_modelo[i]
    cont=0

  print('O modelo ',modelo,'possui ',maior,'veiculos.')  
   
#-----------------------------------------------
def atualizar_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano):
  codigo_atualizar = input("Informe o codigo do veiculo a ser atualizado: ")
  indice = busca(veiculos_codigo, codigo_atualizar)
  if indice != -1:
    v_modelo = input("Informe o novo modelo: ")
    v_ano = input("Informe o novo ano de fabricacao:")
    veiculos_modelo[indice] = v_modelo
    veiculos_ano[indice] = v_ano
    print("Veiculo atualizado com sucesso!")
  else:
    print("\nVeiculo codigo " + codigo_atualizar + " nao encontrado")
#-----------------------------------------------
def remover2(lista, indice):
  ultimo_indice = len(lista) - 1
  lista[indice] = lista[ultimo_indice]
  lista.pop()
#-----------------------------------------------
def remover_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano):
  codigo_remover = input("Informe codigo do veiculo a ser removido: ")
  indice = busca(veiculos_codigo, codigo_remover)
  if indice != -1:
    remover2(veiculos_codigo, indice)
    remover2(veiculos_modelo, indice)
    remover2(veiculos_ano, indice)
    print("Veiculo removido com sucesso!")
  else:
    print("\nVeiculo codigo " + codigo_remover + " nao encontrado")
#-----------------------------------------------
def remover_cliente(cpf_clientes, nome_pessoa, ano_nascimento):
  cpf_remover = int(input("Informe cpf da pessoa a ser removido: "))
  indice = busca(cpf_clientes, cpf_remover)
  if indice != -1:
    remover2(cpf_clientes, indice)
    remover2(nome_pessoa, indice)
    remover2(ano_nascimento, indice)
    print("Veiculo removido com sucesso!")
  else:
    print("\nVeiculo codigo " + cpf_remover + " nao encontrado")
#-----------------------------------------------
def pesquisar_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano):
  codigo_pesquisar = input("Informe o codigo a ser pesquisado: ")
  indice = busca(veiculos_codigo, codigo_pesquisar)
  if indice != -1:
    v_codigo = veiculos_codigo[indice]
    v_modelo = veiculos_modelo[indice]
    v_ano = veiculos_ano[indice]
    print("\nVeiculo codigo: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano))
  else:
    print("\nVeiculo codigo " + codigo_pesquisar + " nao encontrado")
#-----------------------------------------------
def pesquisar_clientes(cpf_clientes, nome_pessoa, ano_nascimento):
  codigo_pesquisar = int(input("Informe o CPF a ser pesquisado: "))
  indice = busca(cpf_clientes, codigo_pesquisar)
  if indice != - 1:
    cpf = cpf_clientes[indice]
    nome = nome_pessoa[indice]
    ano = ano_nascimento[indice]
    print("CPF: {} ,Nome: {} , Nascimento: {} ".format(cpf,nome,ano))
  else:
    print("CPF:",codigo_pesquisar,",não foi encontrado")  
#-----------------------------------------------
def listar_clientes(cpf_clientes, nome_pessoa, ano_nascimento):
  for i in range(len(cpf_clientes)):
    cpf = cpf_clientes[i]
    nome = nome_pessoa[i]
    ano = ano_nascimento[i]
    print("CPF: {} ,Nome: {} , Nascimento: {} ".format(cpf,nome,ano))
#-----------------------------------------------      
def listar_veiculos(veiculos_codigo, veiculos_modelo, veiculos_ano):
  for i in range(len(veiculos_codigo)):
    v_codigo = veiculos_codigo[i]
    v_modelo = veiculos_modelo[i]
    v_ano = veiculos_ano[i]
    print("\nVeiculo codigo: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano)) 
#-----------------------------------------------
def inserir_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano):
  v_codigo = input("Informe o codigo: ")
  
  if busca(veiculos_codigo, v_codigo) == -1:
    v_modelo = input("Informe o modelo: ")
    v_ano = int(input("Informe o ano de fabricacao: "))

    veiculos_codigo.append(v_codigo)
    veiculos_modelo.append(v_modelo)
    veiculos_ano.append(v_ano)
    print("\nVeiculo codigo: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano) + " inserido com sucesso")
  else:
    print("Codigo " + v_codigo + " ja esta cadastrado!")
#-----------------------------------------------
def inserir_cliente(cpf_clientes, nome_pessoa, ano_nascimento):
  cpf = int(input("Informe o CPF:"))
    
  if busca(cpf_clientes, cpf) == -1:
    nome = input("Informe o nome da pessoa:")
    ano = input("Informe o ano de seu nascimento:")
    cpf_clientes.append(cpf)
    nome_pessoa.append(nome)
    ano_nascimento.append(ano)
    print("CPF: {} ,Nome: {} , Nascimento: {} ".format(cpf,nome,ano), "inserido com sucesso")
  else:
      print("O cpf:",cpf,", ja está cadastrado!")
#-----------------------------------------------
def busca(lista, elem):
  i = 0
  while i < len(lista):
    if lista[i] == elem:
        return i
    i = i + 1
  return -1
#-----------------------------------------------
def menu():
  print("\n***************************************")
  print("Gerenciar Veiculos")
  print("   Inserir veiculo.............1")
  print("   Listar veiculos.............2")
  print("   Pesquisar veiculo...........3")
  print("   Atualizar veiculo...........4")
  print("   Remover veiculo.............5")
  print("   Inserir cliente.............6")
  print("   Listar clientes.............7")
  print("   Pesquisar clientes..........8")
  print("   Remover clientes............9")
  print("   Submenu....................10")
  print("Sair do Programa...............0")
  op = input("-> ")
  return op

def sub_menu():
  print("\n****************************************")
  print("Submenu")
  print("   Modelo de veiculo..............1")
  print("   Exibir todos veiculos..........2")
  print("   Exibir veiculo antigo..........3")
  print("   Exibir veiculo novo............4")
  print("   Exibir informações clientes....5")
  print("   Exibir veiculo IPVA............6")
  print("Voltar............................0")
  op = input("-> ")
  return op
#-----------------------------------------------
    
def main():
  # veiculo -> codigo, modelo, ano
  #veiculos_codigo = ['1x', '2x']
  #veiculos_modelo = ['Gol', 'Celta']
  #veiculos_ano =    [2012, 2014]
    
  veiculos_codigo = []
  veiculos_modelo = []
  veiculos_ano = []
  cpf_clientes = []
  nome_pessoa = []
  ano_nascimento = []
   
  opcao = 'x'
  while opcao != '0':

    opcao = menu()
    if opcao == '1':
      inserir_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano)
    elif opcao == '2':
      listar_veiculos(veiculos_codigo, veiculos_modelo, veiculos_ano)
    elif opcao == '3':
      pesquisar_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano)
    elif opcao == '4':
      atualizar_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano)
    elif opcao == '5':
      remover_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano)
    elif opcao == '6':
      inserir_cliente(cpf_clientes, nome_pessoa, ano_nascimento)
    elif opcao == '7':
      listar_clientes(cpf_clientes, nome_pessoa, ano_nascimento)
    elif opcao == '8':
      pesquisar_clientes(cpf_clientes, nome_pessoa, ano_nascimento)
    elif opcao == '9':
      remover_cliente(cpf_clientes, nome_pessoa, ano_nascimento)
    elif opcao == '10':
      nova_opcao = sub_menu()
      if nova_opcao == '1':
        modelo_frequente(veiculos_modelo)
      elif nova_opcao == '2':
        quantidade_modelo(veiculos_modelo)
      elif nova_opcao == '3':
        carro_velho(veiculos_ano ,veiculos_codigo, veiculos_modelo)
      elif nova_opcao == '4':
        carro_novo(veiculos_ano ,veiculos_codigo, veiculos_modelo)
      elif nova_opcao == '5':
        pessoas(ano_nascimento)
      elif nova_opcao == '6':
        ipva(veiculos_ano)
      elif nova_opcao == '0':
        opcao = menu()
      else:
        print("Opcao invalida!!! Escolha novamente!")
    elif opcao == '0':
      print("Obrigado por usar nosso programa!!!")
    else:
      print("Opcao invalida!!! Escolha novamente!")     
#-----------------------------------------------

# Programa principal
main()

#-----------------------------------------------  
