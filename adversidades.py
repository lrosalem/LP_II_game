import random
import time

class Adversidades:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.meteoros = []
        self.velocidade = 0.02  # Defina a velocidade desejada aqui (em segundos)
        self.tempo_ultimo_meteoro = time.time()
        self.historico_meteoros = []  # Histórico das posições dos meteoros

    def gerar_meteoro(self):
        tempo_atual = time.time()
        if tempo_atual - self.tempo_ultimo_meteoro >= self.velocidade:
            x = random.randint(0, self.largura - 1)  # Posição aleatória na largura
            y = 0  # Começa na parte superior da tela
            meteoro = {'x': x, 'y': y}
            self.meteoros.append(meteoro)
            self.tempo_ultimo_meteoro = tempo_atual

    def mover_meteoros(self):
        for meteoro in self.meteoros:
            meteoro['y'] += 1  # Move o meteoro para baixo
            if meteoro['y'] >= self.altura:
                self.meteoros.remove(meteoro)  # Remove meteoros que saem da tela

    def atualizar_adversidades(self):
        tempo_atual = time.time()
        if tempo_atual - self.tempo_ultimo_meteoro >= self.velocidade:
            self.gerar_meteoro()
            self.mover_meteoros()
            self.tempo_ultimo_meteoro = tempo_atual

        self.historico_meteoros.append(list(self.meteoros))  # Adicione uma cópia das posições dos meteoros ao histórico

    def desenhar_adversidades(self, cenario):
        for posicoes in self.historico_meteoros:
            for meteoro in posicoes:
                x = meteoro['x']
                y = meteoro['y']
                if 0 <= x < self.largura and 0 <= y < self.altura:
                    cenario[y][x] = '*'  # Caractere do meteoro no cenário
