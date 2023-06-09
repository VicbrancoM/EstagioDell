import os
import menu
import conta as contabancaria
contas = []
def apresentarmenu():
    print("\n" * os.get_terminal_size().lines)
    print("=====GERENCIAR CONTAS=====")
    print("1 - Cadastrar conta")
    print("2 - Remover conta")
    print("3 - Mesclar contas")
    print("4 - Voltar ao MENU principal")
    opcao= input("Digite sua opção: ")
    switch(opcao)
    
def switch(opcao):
    if opcao == "1":
       cadastrarconta()
    elif opcao == "2":
        print(" Remover conta.")
    elif opcao == "3":
        print("Mesclar contas")
    elif opcao == "4":
        menu.apresentar()
    else:
        print("Opção inválida.")
        input("Digite uma tecla para continuar")
        apresentarmenu()

def cadastrarconta(): 
    print("\n" * os.get_terminal_size().lines)
    print("=====CADASTRAR CONTA=====")
    banco = 0
    while int (banco) < 1 or int (banco) > 999 or len(list(output))!= 3:      
        banco =   input("Digite seu banco[XXX]: ")
        string = str(banco)
        output = map(int, string)
    agencia = "0000000"
    output = map(int, agencia)
    while len(list(output))> 6:  
        agencia =   input("Digite sua agencia: ")
        string = str(agencia)
        output = map(int, string)
    conta = "000000000000000000000"
    output = map(int, conta)
    while len(list(output))> 20:
        conta =   input("Digite sua conta: ")
        string = str(conta)
        output = map(int, string)
    contas.append(contabancaria.conta(banco, agencia, conta))
    print(contas)