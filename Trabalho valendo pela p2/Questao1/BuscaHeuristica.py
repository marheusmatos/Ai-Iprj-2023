
from visual import Visualizavel, visualize
from ProblemaDeBusca import *


class Buscador(Visualizavel):

    def __init__(self, problema):
        self.problema = problema
        self.inicializa_fronteira()
        self.num_expandidos = 0
        self.acrescente_a_fronteira(Caminho(problema.no_de_inicio()))
        super().__init__()

    def inicializa_fronteira(self):
        self.fronteira = []

    def fronteira_vazia(self):
        return self.fronteira == []

    def acrescente_a_fronteira(self, caminho):
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
                            len(self.fronteira), "caminhos restantes na froteira")
                self.solucao = caminho
                return caminho
            else:
                vizi = self.problema.vizin(caminho.fim())
                self.visual(3, "vizinhos sao ", vizi)
                for arco in reversed(list(vizi)):
                    self.acrescente_a_fronteira(Caminho(caminho, arco))
                self.visual(3, "Fronteira:", self.fronteira)
        self.visual(1, "Sem ( mais ) solucoes. Total de",
                    self.num_expandidos, "caminhos  expandidos.")

class BuscaHeuristica(Buscador):
    def heuristica(self, caminho):
        return self.problema.heuristica(caminho.fim())

    def acrescente_a_fronteira(self, caminho):
        self.fronteira.append(caminho)
        self.fronteira.sort(key=self.heuristica, reverse=True)

if __name__ == "__main__":
    pesquisando = BuscaHeuristica(problemaDoAgente)
    cam1=pesquisando.busca()
    while cam1!= None:
        print("--Busca Heuristica - Solucao encontrada:",cam1)
        cam1=pesquisando.busca()
    input('\nPRESSIONE "ENTER" PARA SAIR')