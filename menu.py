import gerenciarcontas
import gerenciartransacoes
import painelgeral
import os

def apresentar():
    print("\n" * os.get_terminal_size().lines)
    print("1 - Gerenciar Contas")
    print("2 - Gerenciar Transações")
    print("3 - Painel geral")
    opcao= input("Digite sua opção: ")
    switch(opcao)
    
def switch(opcao):
    if opcao == "1":

        gerenciarcontas.apresentarmenu()
    elif opcao == "2":
        
        gerenciartransacoes.apresentarmenu()
    elif opcao == "3":
        
        painelgeral.apresentarmenu()
    else:
        print("Opção inválida.")
        input("Digite uma tecla para continuar")
        apresentar()


