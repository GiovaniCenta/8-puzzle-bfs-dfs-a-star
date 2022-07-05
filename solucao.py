from collections import deque
import numpy as np

estado_inicial = "2_3541687"

class Nodo:
    
   

    def __init__(self, estado, pai, acao, custo):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
    
    #função auxiliar pra printar 
    def print_nodo(self):
        print("\n====PRINT NODO ====")
        print("estado = " + str(self.estado) + "\npai = " + str(self.pai) + "\nacao = " + str(self.acao) + "\ncusto = " + str(self.custo))
        print("===================")
        


def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo

    #implementada com as funções esquerda, direita, abaixo (la em baixo no código)
    return [("esquerda",esquerda(estado)), ("direita",direita(estado)),("abaixo",abaixo(estado))]
    


def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    
    esq=Nodo(sucessor(nodo.estado),nodo, )
    dir=
    abaixo= 
    """
    lista_nodos = []
    #custo_filho = nodo.custo
    
    custo = nodo.custo


    #não sei o que fazer quando não tem mais sucessores
    while custo >= 0:
        #retirar da lista de tuplas da funcao sucessor
        suc_esq = sucessor(nodo.estado)[0]
        suc_dir = sucessor(nodo.estado)[1]
        suc_abaixo = sucessor(nodo.estado)[2]
        
        #criar os nodos que seram colocados na lista de nodos sucessores
        esquerda = Nodo(suc_esq[1],nodo,suc_esq[0],custo+1)
        direita = Nodo(suc_dir[1],nodo,suc_dir[0],custo+1)
        abaixo = Nodo(suc_abaixo[1],nodo,suc_abaixo[0],custo+1)
        
        #colocar na lista
        lista_nodos.append(esquerda)
        lista_nodos.append(direita)
        lista_nodos.append(abaixo)
        custo = custo - 1

        #teria que fazer isso para todos os sucessores?
        



    return lista_nodos


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError




def esquerda(estado):
    i = estado.find("_")
    estado = list(estado)
    if(i-1 < 0):
        aux = estado[i]
        aux2 = estado[len(estado)]
        estado[i] = aux2
        estado[len(estado)] = aux
    else:
        aux = estado[i]
        aux2 = estado[i-1]
        estado[i] = aux2
        estado[i-1] = aux
        estado = ''.join(estado)
    return str(estado)


def direita(estado):
    i = estado.find("_")
    estado = list(estado)
    if(i+1 > len(estado)):
        aux = estado[i]
        aux2 = estado[0]
        estado[i] = aux2
        estado[0] = aux
    else:
        aux = estado[i]
        aux2 = estado[i+1]
        estado[i] = aux2
        estado[i+1] = aux
        estado = ''.join(estado)
    return str(estado)

#não sei se ta certa
def abaixo(estado):
    i = estado.find("_")
    estado = list(estado)
    aux = estado[i]
    aux2 = estado[i+3]
    estado[i] = aux2
    estado[i+3] = aux
    estado = ''.join(estado)
    return str(estado)


if __name__ == "__main__":
    node = Nodo(estado_inicial,0,0,0)
    x =expande(node)
    x[0].print_nodo()