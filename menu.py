from cenario import Cenario

class Menu:
    
    def __init__(self):
        self.opcoes = ["Novo Jogo", "High Scores", "Sair"]
        self.linha_grossa = '\u2588'  # Caractere Unicode para o bloco cheio
        self.linha_fina = '\u2500'  # Caractere Unicode para linha horizontal
        self.largura_menu = 50

    def mostrar_menu(self):
        linha_fina = self.linha_fina * self.largura_menu
        linha_grossa = self.linha_grossa * self.largura_menu
        titulo = "Zoroastrēs"
        espacos_laterais = (self.largura_menu - len(titulo)) // 2
        titulo_centralizado = ' ' * espacos_laterais + titulo + ' ' * espacos_laterais

        print(f"\033[34m{linha_grossa}\033[m")  # Linha grossa azul
        print(f"\033[37m{titulo_centralizado}\033[m")  # Texto com a cor branca
        print(f"\033[34m{linha_fina}\033[m")  # Linha fina azul

        for i, opcao in enumerate(self.opcoes, start=1):
            print(f"{i}. {opcao}") 

        print(f"\033[34m{linha_fina}\033[m")  # Linha fina azul

    def iniciar_jogo(self):
        print("Novo jogo iniciado. Boa sorte! \n")
        cenario = Cenario(50, 20)  # Crie uma instância do cenário com a largura e altura desejadas
        cenario.iniciar_jogo()  # Inicie o jogo no cenário

    def mostrar_high_scores(self):
        print("High Scores:")
        
        # Inserir aqui a chamada da classe high scores;

    def sair_do_jogo(self):
        linha_fina = self.linha_fina * self.largura_menu  
        linha_grossa = self.linha_grossa * self.largura_menu
        print("Saindo do jogo. Até a próxima!")
        print(f"\033[34m{linha_grossa}\033[m")  # Linha grossa azul
