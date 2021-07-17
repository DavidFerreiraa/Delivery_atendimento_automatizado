from time import sleep
from os import system
from datetime import datetime


def cadastrar():
  login = False
  while not login:
    print('''\033[44m Digite o número correspondente \033[m\n     \033[44m à opção que deseja: \033[m
  
    \033[32m1\033[m - \033[36mLogin\033[m
    \033[32m2\033[m - \033[36mRealizar cadastro\033[m
''', end=' ')
  
    while True:
      logou = False
      cadalogin = input('\n\033[32m>>>\033[m\033[33m ')
      system('clear')
      print('\033[m')

      if cadalogin.isnumeric():
        cadalogin = int(cadalogin)
        if 1 <= cadalogin <= 2:
          logou = True
          break

      if not logou:
        print('\033[43m Valor inválido! \033[m\n')
        print('''\033[44m Digite o número correspondente \033[m\n     \033[44m à opção que deseja: \033[m
  
    \033[32m1\033[m - \033[36mLogin\033[m
    \033[32m2\033[m - \033[36mRealizar cadastro\033[m
''', end=' ')
    
    if cadalogin == 1: # pede as informações do usuário para verificar se já está cadastrado.
      with open('cadastros.txt', 'r') as arquivo:
        print("  \033[46m REALIZANDO LOGIN... \033[m\n")

        nome = input("\n\033[40;37;1m Nome do Usuário: \033[m\033[33m ").strip().title().replace(' ', '')
        senha = input("\033[m\033[40;37;1m Senha: \033[m\033[33m ").replace(" ", "")
        print("\033[m")
        nomesenha = str(f'{nome};{senha}')
        
        for linha in arquivo: 
          if linha.strip() == nomesenha: # Caso o login seja bem sucedido
            print("\n\033[32m Login bem sucedido! \033[m\n\n\033[44m Espere um momento. \033[m")
            sleep(3)
            system('clear')
            login = True
            break
        # Caso o login não seja bem sucedido  
        if not login:
          print("Você \033[41m NÃO \033[m está cadastrado.\nConfira se o nome e senha estão corretos.\n")
      arquivo.close()

    elif cadalogin == 2: # Cadastra o usuário
        print("  \033[46m REALIZANDO CADASTRO... \033[m\n")

        cadastrou = False
        while not cadastrou:
          with open('cadastros.txt', 'r+') as arq:
            cadastrado = False
            nome_cadastro = input("\n\033[40;37;1m Nome de login: \033[m\033[33m ").strip().title()
            print('\033[m', end="")

            for linha in arq: # Identifica se ja existe algum usuário com este nome
              if nome_cadastro == linha.split(';')[0]:
                print("\n\033[41m Já tem um usuário com este nome, tente novamente com outro nome. \033[m\n")
                cadastrado = True
                break
            if not cadastrado:
              cadastrou = True
          arq.close()
          
        
        with open('cadastros.txt', 'a') as arq: # Envia as informações para o arquivo
          senha_cadastro = input("\033[40;37;1m Senha: \033[m\033[33m ").replace(' ', '').strip()
          print('\033[m')
          nomesenha_cadastro = f'{nome_cadastro};{senha_cadastro}'
          arq.write('\n' + nomesenha_cadastro + '\n')
          arq.close()
        #Cadastra o endereço do usuário
        with open('enderecos.txt', 'a') as end:
          print("\nAgora, iremos \033[33mcadastrar\033[m \no \033[33mendereço de entrega\033[m.")

          bairro = str(input('\nPrimeiro, digite abaixo \napenas o \033[36mNome do Bairro\033[m:\n \033[32m\n>>>\033[m ')).strip().title()
          rua = str(input('\nAgora, digite abaixo\napenas o \033[36mNome da Rua\033[m:\n \033[32m\n>>>\033[m R.')).strip().title()
          print('\nE por último, digite\nabaixo algum \033[36mIncremento\033[m')
          numero = str(input('sobre o local de entrega.\n(\033[31mNúmero \033[mou \033[31mCor\033[m)\n \033[32m\n>>>\033[m ')).strip().title()
          
          nomeendereco_cadastro = f'{nome_cadastro};{bairro};{rua};{numero}'
          end.write('\n' + nomeendereco_cadastro + '\n')
          system('clear')
          print("\033[32m Cadastro bem sucedido! \033[m\n")
          cadastrou = True
          end.close()
  # Retorna o nome do usuário
  return nome
# Recepciona o cliente
def recepcao(): # Função para mensagem de recepção simples.
    print("\n \033[44m Seja bem-vindo(a) a pastelaria Ifal! \n\n\033[m      \033[44m Aguarde alguns instantes. \n\033[m")
    for contador in range(3):
        print(' .')
        sleep(0.2)
    system('clear')

# Mostra o cardápio (Organiza melhor o def realizar_pedido)
def cardapio():
  print(''' =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=    
  
            - \033[43m CARDÁPIO \033[m - 

  1. \033[36mTrês queijos\033[m        2. \033[36mMisto\033[m
    \033[32mR$\033[m8,00                 \033[32mR$\033[m5,00

  3. \033[36mCalabresa\033[m           4. \033[36mFrango\033[m
    \033[32mR$\033[m6,00                 \033[32mR$\033[m6,00           

  5. \033[36mPizza\033[m               6. \033[36mQueijo\033[m
    \033[32mR$\033[m8,00                 \033[32mR$\033[m5,00  

  7. \033[36mCarne com Cheddar\033[m   8. \033[36mBacon\033[m
    \033[32mR$\033[m8,00                 \033[32mR$\033[m7,00
 
 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')

def nome_dat_endere(nome, arq_enderec):
  print(f"\n\nOlá, \033[32m{nome}\033[m!")
  
  # Informa dia, mês e ano ao usuário (nesta ordem)
  print(f'\nData: \033[32m{datetime.now().day}\033[m / \033[32m{datetime.now().month}\033[m / \033[32m{datetime.now().year}\033[m')

  with open('enderecos.txt', 'r') as arquivo: #Mostra o endereço cadastrado
    for linha in arquivo:
      if nome == linha.replace('[]', '').replace(" ' ", '').split(';')[0].strip(): 
        print(f'\nEndereço de entrega atual:\n')
        for contador in range(1, 4):
          print(f'\033[32m{linha.split(";")[contador]}\033[m', end='')
          if contador < 3:
            print(end=', ')

def realizar_pedido(): # Realiza o pedido do cliente
  nomes_pasteis = {0 : 'Três queijos', 1 : 'Misto', 2 : 'Calabresa', 3 : 'Frango', 4 : 'Pizza', 5 :'Queijo', 6 : 'Carne com cheddar', 7 : 'Bacon'}
  nome = cadastrar() # Recebe o nome do usuário e faz o cadastro
  
  for contador in range(5): # Imprime a mensagem de recepção
    recepcao()
  
  cardapio() # Imprime o cardápio com cores

  opcoes = [[0, 8], [0, 5], [0, 6], [0, 6], [0, 8], [0, 5], [0, 8], [0, 7]] # Lista para quantidade e preço
  pedindo = True
  while pedindo: # Laço para continuar rodando o programa.
    erro = False # Condição.
    system('clear')
      
    cardapio() # Imprime o cardápio com cores.
    nome_dat_endere(nome, 'enderecos.txt')
    
    print('\n\n\033[41m OBS: \033[m \033[33mVocê pode mudar o endereço\n       de entrega após fazer o pedido.\033[m')
      
    print('''\033[44m\n\n Digite "0" para finalizar, e logo após \033[m\n  \033[44m escolher a forma de pagamento. \033[m
      \n\033[44m Digite "REMOVER" para remover algum \033[m\n    \033[44m item que foi solicitado. \033[m\n''')
    pedido = str(input('\033[41m Digite abaixo o número correspondente \033[m\n      \033[41m à opção que você deseja. \033[m\n\n\033[32m>>>\033[33m ')) # Variável para fazer o pedido.
    print('\033[m')

    contador = 0 # Calcular quantas vezes cada sabor foi pedido.
    if pedido.isnumeric():
      pedido = int(pedido) #Transforma o pedido em inteiro caso seja um valor numérico
        
      while 8 >= pedido > 0: #Recebe o pedido do cliente e altera a quantidade
        contador += 1
        if pedido == contador:
          opcoes[contador-1][0] += 1
          system('clear')
          break    
      else:
        while pedido == 0 : # Quando o usuário parar de fazer os pedidos (Digitando 0)
          system('clear')

          # Confirmar se o usuário não deseja algum pastel a mais.
          
          confirmar = input('''\n\n \033[41m Tem certeza de que não quer \033[m\n   \033[41m algum pastel a mais? \033[m 
          
   \033[46m Digite abaixo o número \033[m\n  \033[46m correspondente a opção. \033[m

     1. \033[32mSim\033[m        2. \033[31mNão\n\n\033[32m>>>\033[33m ''')
          print('\033[m')
          if confirmar.isnumeric():
            confirmar = int(confirmar)
          valor_total = 0 # Calcular o preço total.
          for cada_pastel in opcoes:
            valor_total += cada_pastel[0] * cada_pastel[1]
              
          if confirmar == 1 and valor_total > 0: # Escolher o meio de pagamento
            print(f'\nValor total dos pastéis:\033[32m {valor_total}\n\033[mNo cartão: \033[32m{valor_total + 2}\n\033[m')
            nomes_pagamento = {1 : 'Dinheiro', 2 : 'Cartão', 3 : 'PIX'}
            
            with open('enderecos.txt', 'r') as arquivo: #Mostra o endereço cadastrado
              for linha in arquivo:
                if nome == linha.replace('[]', '').replace(" ' ", '').split(';')[0].strip(): 
                  print(f'\nEndereço de entrega atual:\n')
                  for contador in range(1, 4):
                    print(f'\033[32m{linha.split(";")[contador]}\033[m', end='')
                    if contador < 3:
                      print(end=', ')

            print('\n\n\033[33mDigite\033[31m 0\033[33m caso deseje alterar\n     seu endereço.\033[m\n')
            print('\033[46m Digite abaixo o número correspondente \033[m\n     \033[46m à forma de pagamento. \033[m')

            forma_pagamento = input('\n\033[m \n  1 - \033[32mDinheiro\n\033[m  2 - \033[32mCartão\n\033[m  3 - \033[32mPix\n\n>>>\033[m ') #Recebe qual será a forma de pagamento utilizada pelo cliente
            if forma_pagamento.isnumeric():
              forma_pagamento = int(forma_pagamento)
            if forma_pagamento == 1:
              print(f'\n- \033[32m{nomes_pagamento[forma_pagamento]}\033[m')
              pedindo = False
              break
            elif forma_pagamento == 2:
              print(f'\n- \033[32m{nomes_pagamento[forma_pagamento]}\033[m')
              pedindo = False
              break
            elif forma_pagamento == 3:
              print(f'\n- \033[32m{nomes_pagamento[forma_pagamento]}\033[m')
              pedindo = False
              break
            elif forma_pagamento == 0:
              with open('enderecos.txt', 'r+') as end:
                novo_bairro = str(input('\nPrimeiro, digite abaixo \napenas o \033[36mNome do Bairro\033[m:\n \033[32m\n>>>\033[m ')).strip().title()
                nova_rua = str(input('\nAgora, digite abaixo\napenas o \033[36mNome da Rua\033[m:\n \033[32m\n>>>\033[m R.')).strip().title()
                print('\nE por último, digite\nabaixo algum \033[36mIncremento\033[m')
                novo_numero = str(input('sobre o local de entrega.\n(\033[31mNúmero \033[mou \033[31mCor\033[m)\n \033[32m\n>>>\033[m ')).strip().title()
                with open('enderecos.txt', 'r+') as end1: #Altera o endereço do cliente
                  for linha in end1:
                    if nome == linha.split(';')[0]:
                      ant_endereco = linha
                      ant_endere = ant_endereco.split(';')[:]
                      ant_endere[0] = nome
                      ant_endere[1] = novo_bairro
                      ant_endere[2] = nova_rua
                      ant_endere[3] = novo_numero
                      novo_endereco = str(ant_endere).replace('[', '').replace(']', '').replace(',', ';').replace("'", "")

                end1.close()
                entrou = False

                with open('enderecos.txt', 'r') as end2:
                  linhas_ = end2.readlines()
                  end2.close()
                  with open('enderecos.txt', 'w') as end3:
                    for cada_linha in linhas_:
                      if cada_linha == '':
                        pass
                      elif str(cada_linha) == str(ant_endereco).replace('[', '').replace(']', '').replace(',', ';').replace("'", ""):
                        end3.write( novo_endereco.replace('[', '').replace(']', '').replace(',', ';').replace("'", ""))
                        entrou = True
                      elif entrou:
                        end3.write('\n'+cada_linha)
                      else:
                        end3.write(cada_linha)
                    print('\n\033[32mNovo endereço cadastrado com sucesso!!!\033[m')
                    sleep(3)
                  end3.close()
            else:
              print('\n\033[33mOops! Valor inválido, digite novamente.\n\033[m')
              sleep(1.5)
              system('clear')
      
          elif confirmar == 1 and valor_total == 0 : # Caso o usuário pedir nada.
            pedindo = False
            break

          elif confirmar == 2: # Caso o usuário quiser voltar para o cardápio.
            break

          else:
            print('\n\033[33mOops! Valor inválido, digite novamente.\n\033[m')
            sleep(2)
            system('clear')

        else:
          erro = True
          print('\n\033[33mOops! Valor inválido, digite novamente em 3 segundos.\n\033[m')
          sleep(3)
          system('clear')

      if not erro:
        for contador in range(8): # Impressar quantas vezes cada sabor foi pedido.
          if opcoes[contador][0] != 0 :
            print(f'\n\n- Você pediu \033[32m{opcoes[contador][0]}\033[m vez(es) de \033[36m{nomes_pasteis[contador]}\033[m.')
            sleep(1)       
      sleep(1.5)

    while str(pedido).upper().strip().replace(' ', '') == 'REMOVER':
      system('clear')
      cardapio()
      for contador, cada_pastel in enumerate(opcoes):
        if cada_pastel[0] > 0:
          print(f'\n\n- Você pediu \033[32m{cada_pastel[0]}\033[m vez(es)de \033[36m{nomes_pasteis[contador]}\033[m.')
        
      print('''\n\n\033[46m Digite abaixo o número correspondente à \033[m\n   \033[46m opção que deseja remover.''', end="")
      print(' Caso \033[m\n      \033[46m queira voltar digite 0. \033[m\n')
      print('\033[41m OBS: \033[m\033[33m Confira se o número que você vai\n       digitar corresponde a uma opção\n       que JÁ FOI SOLICITADA', end='')
      print(', caso contrário\n       o programa não irá fazer nada.\033[m')

      resposta = input('\n\033[32m>>>\033[33m ')
      print('\033[m')
      if resposta.isnumeric() and 0 <= int(resposta) <= 8:
        resposta = int(resposta)
        if resposta == 0:
          break
        for cada_nome in nomes_pasteis.keys():
          entrou = False
          if resposta == cada_nome and opcoes[cada_nome-1][0] > 0:
            opcoes[cada_nome-1][0] -= 1
            print("\033[31mRemovendo em 3 segundos...\033[m")
            sleep(2)
            entrou = True
            break
            
        if not entrou:
          print('\033[41m Essa opção não foi solicitada antes \033[m')
          print('\033[41m ou você já removeu o item, logo, não \033[m\n\033[41m podemos remove-la. Tente \033[m', end='')
          print('\033[41m novamente \033[m\n       \033[41m após 3 segundos. \033[m')
          sleep(3)
              
      else:
        print('\n\033[43m Valor inválido! Digite novamente \033[m\033[m\n      \033[43m após 3 segundos. \033[m')
        sleep(3)
