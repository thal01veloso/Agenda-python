def menu():
  voltarMenuPrincipal = 's'
  while voltarMenuPrincipal=='s':
    opcao= input(f'''
  =================================================================
                    PROJETO AGENDA EM PYTHON                v.1
                                +
                                + {contarContatos()} CONTATOS CADASTRADOS
                                +
  MENU:                         + ÚLTIMO CADASTRO
                                + {ultimoContatoCadastrado()}
  [1]CADASTRAR CONTATO          +
  [2]LISTAR CONTATO             +
  [3]DELETAR CONTATO            +     
  [4]BUSCAR CONTATO PELO NOME   +
  [5]ATUALIZAR CONTATO          +
  [6]SAIR                       +
                                +
  ==================================================================

  ESCOLHA UMA OPÇÃO ACIMA: 
  
  ''')
    if opcao =="1":
      cadastrarContato()
    elif opcao== "2":
      listarContato()
    elif opcao =="3":
      deletarContato()
    elif opcao=="4":
      buscarContatoPeloNome()
    elif opcao =='5':
      atualizarContato()
    elif opcao =='6':
      sair()
    else:
      print("Opção inválida")
      menu()
    voltarMenuPrincipal=input("Deseja voltar ao menu principal ? (s/n) ").lower()
    
def contarContatos():
  with(open("agenda.txt","r")) as agenda:
    return len(agenda.readlines())

def atualizarContato():
  nomeDeletado = input("Digite o nome para ser Atualizado: ").lower()
  agenda = open("agenda.txt","r")
  aux = []
  aux2= []
  for i in agenda:
    aux.append(i)
  for i in range(0, len(aux)):
    if nomeDeletado not in aux[i].lower():
      aux2.append(aux[i])
  agenda = open("agenda.txt","w")
  for i in aux2:
    agenda.write(i)
  idContato = input("Escolha o Id do contato atualizado: ")
  nome = input("Escreva o nome do contato atualizado: ")
  telefone = input("Escreva o telefone do contato atualizado: ")
  email = input("Escreva o email do contato atualizado: ")
  try:
    agenda = open("agenda.txt","a")
    dados = f'{idContato};{nome};{telefone};{email} \n'
    agenda.write(dados)
    agenda.close()
    print(f'Contato Atualizado com sucesso !!!!')
  except:
    print("ERRO na gravação do contato")
  
  

def cadastrarContato():
  idContato = input("Escolha o Id do contato: ")
  nome = input("Escreva o nome do contato: ")
  telefone = input("Escreva o telefone do contato: ")
  email = input("Escreva o email do contato: ")
  try:
    agenda = open("agenda.txt","a")
    dados = f'{idContato};{nome};{telefone};{email} \n'
    agenda.write(dados)
    agenda.close()
    print(f'Contato gravado com sucesso !!!!')
  except:
    print("ERRO na gravação do contato")

def listarContato():
  agenda = open("agenda.txt","r")
  for contato in agenda:
    print(f'{contato.split(";")[0]}  {contato.split(";")[1]}  {contato.split(";")[2]}  {contato.split(";")[3]}')
  agenda.close()

def deletarContato():
  nomeDeletado = input("Digite o nome para ser deletado: ").lower()
  agenda = open("agenda.txt","r")
  aux = []
  aux2= []
  for i in agenda:
    aux.append(i)
  for i in range(0, len(aux)):
    if nomeDeletado not in aux[i].lower():
      aux2.append(aux[i])
  agenda.close()
  agenda = open("agenda.txt","w")
  for i in aux2:
    agenda.write(i)
  print(f'contato deletado com sucesso')
  listarContato()
  
def buscarContatoPeloNome():
  nome=input(f'digite o nome a ser procurado: ').upper()
  agenda = open("agenda.txt","r")
  for contato in agenda:
    if nome in contato.split(";")[1].upper():
      print(contato)
  agenda.close()
def ultimoContatoCadastrado():
  with(open("agenda.txt","r")) as contatos:
    ultimoContato= contatos.readlines()[-1]
    return ultimoContato
    
def sair():
  print(f'Até mais... !!!')
  exit()

 


def main():

  menu()

main()
