from menu import Menu
from cenario import Cenario

if __name__ == "__main__":
    menu = Menu()
    cenario = None  

    while True:
        menu.mostrar_menu()  

        escolha = input("Entre com a opção desejada: ")

        if escolha == "1":
            if cenario is None:
                cenario = Cenario(50, 20) 
            menu.iniciar_jogo()
        elif escolha == "2":
            menu.mostrar_high_scores()
        elif escolha == "3":
            menu.sair_do_jogo()
            break
        else:
            print("Opção inválida. Escolha novamente.")
