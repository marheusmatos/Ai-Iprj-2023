from visual import Visualizavel, visualize
from ProblemaDeBusca import *


class BuscadorPersonalizado(Visualizavel):
    """
    Esta classe representa um buscador para um problema.
    Um caminho é formado ao chamar várias vezes o buscador.
    Realiza a busca em profundidade.
    """

    def __init__(self, problema):
        self.problema = problema
        self.fronteira = []
        self.num_expandidos = 0
        self.adicionar_a_fronteira(Caminho(problema.no_de_inicio()))
        super().__init__()

    def inicializar_fronteira(self):
        self.fronteira = []

    def fronteira_vazia(self):
        return len(self.fronteira) == 0

    def adicionar_a_fronteira(self, caminho):
        self.fronteira.append(caminho)

    @visualize
    def busca(self):

        while not self.fronteira_vazia():
            caminho = self.fronteira.pop()
            self.visual(1, "Expandindo:", caminho,
                        "(custo:", caminho.custo, ")")
            self.num_expandidos += 1
            if self.problema.eh_objetivo(caminho.fim()):
                self.visual(1, self.num_expandidos, "caminhos expandidos e ",
                            len(self.fronteira), "caminhos restantes na fronteira")
                self.solucao = caminho
                return caminho
            else:
                vizinhos = self.problema.vizin(caminho.fim())
                self.visual(3, "vizinhos são ", vizinhos)
                for arco in reversed(list(vizinhos)):
                    self.adicionar_a_fronteira(Caminho(caminho, arco))
                self.visual(3, "Fronteira:", self.fronteira)
        self.visual(1, "Sem mais soluções. Total de",
                    self.num_expandidos, "caminhos expandidos.")


class BuscaAStar(BuscadorPersonalizado):
    def custo_total(self, caminho):
        return caminho.custo + self.problema.heuristica(caminho.fim())

    def adicionar_a_fronteira(self, caminho):
        self.fronteira.append(caminho)
        self.fronteira.sort(key=self.custo_total, reverse=True)


if __name__ == "__main__":
    buscador_customizado = BuscaAStar(problemaDoAgente)
    caminho_atual = buscador_customizado.busca()
    while caminho_atual is not None:
        print("--Busca A* - Solução encontrada:", caminho_atual)
        caminho_atual = buscador_customizado.busca()
    input('\nPRESSIONE "ENTER" PARA SAIR')
