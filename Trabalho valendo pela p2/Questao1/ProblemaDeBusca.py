
class Busca_problema(object):

    def no_de_inicio(self):
        raise NotImplementedError("no_de_inicio")   
    
    def eh_objetivo(self,no):
        raise NotImplementedError("eh_objetivo")  

    def vizin(self,no):
        raise NotImplementedError("vizin")   

    def heuristica(self,n):
        return 0

class arco(object):
    def __init__(self, partida_no, chegada_no, custo=1, acao=None):
        assert custo >= 0, ("Custo nao pode ser negativo "+
                           str(partida_no)+"->"+str(chegada_no)+", custo: "+str(custo))
        self.partida_no = partida_no
        self.chegada_no = chegada_no
        self.acao = acao
        self.custo=custo

    def __repr__(self):
        if self.acao:
            return str(self.partida_no)+" --"+str(self.acao)+"--> "+str(self.chegada_no)
        else:
            return str(self.partida_no)+" --> "+str(self.chegada_no)

class Problema_busca_com_grafo_explicito(Busca_problema):
    def __init__(self, nos, arcos, inicio=None, objetivos=set(), hmap={}, posicoes={}):
        self.vizinhos = {}
        self.nos = nos
        for no in nos:
            self.vizinhos[no]=[]
        self.arcos = arcos
        for arco in arcos:
            self.vizinhos[arco.partida_no].append(arco)
        self.inicio = inicio
        self.objetivos = objetivos
        self.hmap = hmap
        self.posicoes = posicoes

    def no_de_inicio(self):
        return self.inicio
    
    def eh_objetivo(self,no):
        return no in self.objetivos

    def vizin(self,no):
        return self.vizinhos[no]

    def heuristic(self,no):
        if no in self.hmap:
            return self.hmap[no]
        else:
            return 0
        
    def __repr__(self):
        res=""
        for arco in self.arcos:
            res += str(arco)+".  "
        return res

    def nos_vizinhos(self,no):
        return (caminho.chegada_no for caminho in self.vizinhos[no])

class Caminho(object):
    
    def __init__(self,inicio,arco=None):
        self.inicio = inicio
        self.arco=arco
        if arco is None:
            self.custo=0
        else:
            self.custo = inicio.custo+arco.custo

    def fim(self):
        if self.arco is None:
            return self.inicio
        else:
            return self.arco.chegada_no

    def nos(self):
        atual = self
        while atual.arco is not None:
            yield atual.arco.chegada_no
            atual = atual.inicio
        yield atual.inicio

    def initial_nodes(self):

        if self.arco is not None:
            yield from self.inicio.nos()
        
    def __repr__(self):

        if self.arco is None:
            return str(self.inicio)
        elif self.arco.acao:
            return (str(self.inicio)+"\n   --"+str(self.arco.acao)
                    +"--> "+str(self.arco.chegada_no))
        else:
            return str(self.inicio)+" --> "+str(self.arco.chegada_no)


problemaDoAgente = Problema_busca_com_grafo_explicito(
    {'correio','ts','o103','o109','o111','b1','b2','b3','b4','c1','c2','c3',
     'o125','o123','o119','r123','almoxarifado'},
     [arco('ts','correio',6),
        arco('o103','ts',8),
        arco('o103','b3',4),
        arco('o103','o109',12),
        arco('o109','o119',16),
        arco('o109','o111',4),
        arco('b1','c2',3),
        arco('b1','b2',6),
        arco('b2','b4',3),
        arco('b3','b1',4),
        arco('b3','b4',7),
        arco('b4','o109',7),
        arco('c1','c3',8),
        arco('c2','c3',6),
        arco('c2','c1',4),
        arco('o123','o125',4),
        arco('o123','r123',4),
        arco('o119','o123',9),
        arco('o119','almoxarifado',7)],
    inicio = 'o103',
    objetivos = {'r123'},
    hmap = {
        'correio' : 26,
        'ts' : 23,
        'o103' : 21,
        'o109' : 24,
        'o111' : 27,
        'o119' : 11,
        'o123' : 4,
        'o125' : 6,
        'r123' : 0,
        'b1' : 13,
        'b2' : 15,
        'b3' : 17,
        'b4' : 18,
        'c1' : 6,
        'c2' : 10,
        'c3' : 12,
        'almoxarifado' : 12
        }
    )
