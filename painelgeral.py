import os
import menu

def apresentarmenu():
    print("\n" * os.get_terminal_size().lines)
    print("=====PAINEL GERAL=====")
    print("1 - Resumo das contas")
    print("2 - Resumo de receitas e despesas do mês")
    print("3 - Saldo geral dos últimos 6 meses")
    print("4 - Simulação de investimento")
    print("5 - Voltar ao MENU principal")

    opcao= input("Digite sua opção: ")
    switch(opcao)
    
def switch(opcao):
    if opcao == "1":
        print("Resumo das contas.")
    elif opcao == "2":
        print("Resumo de receitas e despesas do mês.")
    elif opcao == "3":
        print("Saldo geral dos últimos 6 meses")
    elif opcao == "4":
        print("Simulação de investimento")
    elif opcao == "5":
        menu.apresentar()
    else:
        print("Opção inválida.")
        input("Digite uma tecla para continuar")
        apresentarmenu()
