import os
import menu

def apresentarmenu():
    print("\n" * os.get_terminal_size().lines)
    print("=====GERENCIAR TRANSAÇÕES=====")
    print("1 - Extrato da conta")
    print("2 - Incluir transação")
    print("3 - Editar a última transação")
    print("4 - Transferir fundos")
    print("5 - Voltar ao MENU principal")

    opcao= input("Digite sua opção: ")
    switch(opcao)
    
def switch(opcao):
    if opcao == "1":
        print("Extrato da conta.")
    elif opcao == "2":
        print("Incluir transação.")
    elif opcao == "3":
        print("Editar a última transação.")
    elif opcao == "4":
        print("Transferir fundos.")
    elif opcao == "5":
        menu.apresentar()
    else:
        print("Opção inválida.")
        input("Digite uma tecla para continuar")
        apresentarmenu()
