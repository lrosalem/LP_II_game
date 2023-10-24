import os
import time
import random

class Cenario:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.cenario = [[' ' for _ in range(largura)] for _ in range(altura)]
        self.adversidades = []

    def limpar_cenario(self):
        for i in range(self.altura):
            for j in range(self.largura):
                self.cenario[i][j] = ' '

    def mostrar_cenario(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        # Desenhe as adversidades no cenário
        for adversidade in self.adversidades:
            x, y, caractere = adversidade
            self.cenario[y][x] = caractere

        output = '*' * (self.largura + 2) + '\n'
        for i in range(self.altura):
            output += '*'
            for j in range(self.largura):
                output += self.cenario[i][j]
            output += '*\n'
        output += '*' * (self.largura + 2) + '\n'
        print(output)

    def adicionar_adversidade(self, x, y, caractere):
        self.adversidades.append((x, y, caractere))

    def gerar_adversidade_aleatoria(self):
        x = random.randint(0, self.largura - 1)  # Posição aleatória na largura
        y = 0  # Começa na parte superior da tela
        caractere = '*'  # Caractere da adversidade (por exemplo, '*')
        self.adicionar_adversidade(x, y, caractere)

    def mover_adversidades(self):
        # Mova as adversidades para baixo
        for i in range(len(self.adversidades)):
            x, y, caractere = self.adversidades[i]
            y += 1  # Move para baixo
            self.adversidades[i] = (x, y, caractere)

    def iniciar_jogo(self):
        numero_de_iteracoes = 10  # Defina o número desejado de iterações da rodada
        for iteracao in range(numero_de_iteracoes):
            self.gerar_adversidade_aleatoria()  # Gere uma nova adversidade aleatória

            self.mostrar_cenario()  # Mostre o cenário atual
            time.sleep(0.1)  # Aguarde um curto período de tempo para simular o movimento

            self.mover_adversidades()  # Movimente as adversidades

            if iteracao == 9:  # Termina o jogo após 10 iterações (0 a 9)
                print("Fim do jogo!")
                break

if __name__ == "__main__":
    cenario = Cenario(20, 10)  # Crie uma instância do cenário com a largura e altura desejadas
    cenario.iniciar_jogo()  # Inicie o jogo no cenário
