
from queue import PriorityQueue
import time
estado_inicial = "2_3541687"
lista_nodos = []
lista_esq = []
lista_dir = []
lista_abaixo = []
from collections import deque

class Nodo:
    
    def __lt__(self, nodo):
        return self.custo < nodo.custo
    def __init__(self, estado, pai, acao, custo):
     
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
    
    #função auxiliar pra printar 
    def print_nodo(self):
        print("\n====PRINT NODO ====")
        print("estado = " + str(self.estado) + "\npai = " + str(self.pai) + "\nacao = " + str(self.acao) + "\ncusto = " + str(self.custo))
        print("===================")
        

def achaunderline(Lestado):
    return Lestado.index("_")

def sucessor(estado):
    #tem que transformar em lista, problemas com string
    Lestado = list(estado)
    #movimenta(Lestado,tipo_mov,posicoes_sem_movimento,movimento)
    sucessores = [movimenta(Lestado,"esquerda",[0,3,6],-1), movimenta(Lestado,"direita",[2,5,8],+1),movimenta(Lestado,"acima",[0,1,2],-3),movimenta(Lestado,"abaixo",[6,7,8],+3)]
    #retirar os Nones -> movimentos inválidos
    sucessores = list(filter(None, sucessores))
    

    return sucessores
    
def expande(nodo):
    lista_nodos = []
    sucessores = sucessor(nodo.estado)
    for suc in sucessores:
        acao = suc[0]
        estado = suc[1]
        pai = nodo
        custo = nodo.custo+1
        nodoSucessor = Nodo(estado,pai,acao,custo)
        lista_nodos.append(nodoSucessor)
    return lista_nodos
            

def percorreCaminho(nodoAtual):
    caminho =[]
    
    while nodoAtual.pai:
        #print("entrou aqui")
        #inserir no começo da lista pra ter a ordem certa
        caminho.insert(0,nodoAtual.acao)
        nodoAtual = nodoAtual.pai
    return caminho
        
def printa_resultado(algoritmo,tempo,Nexpandidos,custo):
    print("===== Algoritmo " + str(algoritmo) + "=====")
    print("Tempo de exec: " + str(tempo))
    print("Numero de nós expandidos: " + str(Nexpandidos))
    print("Custo: " + str(custo))


def movimenta(Lestado,tipo_mov,posicoes_sem_movimento,movimento):
        
    posunderline = achaunderline(Lestado)
    auxLestado = Lestado[:]
    if posunderline in posicoes_sem_movimento:
        return None
    else:
        auxLestado[posunderline] = auxLestado[posunderline+movimento]
        auxLestado[posunderline+movimento] = "_"
        estado = "".join(auxLestado)
        return (tipo_mov,estado)


def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

#########################################################

def hasSolution(string):
	inversions = 0
	for i in range (0, 9):
		for j in range (i+1,9):
			if string[i] != "_" and string[j] != "_" and string[i] and string[j] < string[i]:
				inversions += 1
	if inversions % 2 == 0:
		return 1
	else:
		return 0

def bfs(estado):
    
    t1 = time.time()
    algoritmo = "BFS"
    Nexpandidos = 0
    fronteira = []
    explorado = set()
    nodo_inicial = Nodo(estado,None,None,1)
    fronteira.append(nodo_inicial)
    
    
    #print(fronteira)
    
    
    while fronteira:         
        nodoAtual = fronteira[0]
        fronteira.pop(0)

        if nodoAtual.estado == "12345678_":
            caminho = percorreCaminho(nodoAtual)
            #print(caminho)
            t2 = time.time()
            tempo = t2 - t1
            
            custo = len(caminho)
            printa_resultado(algoritmo,tempo,Nexpandidos,custo)
            return caminho

            
            
        if nodoAtual.estado not in explorado:
            explorado.add(nodoAtual.estado)
            sucessores = expande(nodoAtual)
            Nexpandidos = Nexpandidos + len(sucessores)
           
            fronteira.extend(sucessores)

    print("Não há solução no algoritmo " + algoritmo + " para o estado inicial" + estado)
    return None
      




def dfs(estado):
    t1= time.time()
    algoritmo = "DFS"
    NExpandidos = 0
    fronteira = []
    explorados = set()
    
    if(hasSolution(estado) == 0):
        print("Não há solução DFS para o estado: " + estado )
        return None

    nodoInicial = Nodo(estado,None,None,1)
    fronteira.append(nodoInicial)
    
    while fronteira:
        nodoAtual = fronteira.pop()

        if nodoAtual.estado not in explorados:
            sucessores = expande(nodoAtual)
            NExpandidos = NExpandidos + len(sucessores)
            explorados.add(nodoAtual.estado)
            fronteira.extend(sucessores)

        if nodoAtual.estado == "12345678_":
            caminho = percorreCaminho(nodoAtual)
            #print(caminho)
            t2 = time.time()
            tempo = t2 - t1
            algoritmo = "DFS"
            custo = len(caminho)
            printa_resultado(algoritmo,tempo,NExpandidos,custo)
            return caminho
            
            
    print("Não há solução no algoritmo " + algoritmo + " para o estado inicial" + estado)
    return None

  
  
def astar_hamming(estado):
    """"
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    t1 = time.time()
    Nexpandidos = 0
    fronteira = []
    explorado = set()
    nodo_inicial = Nodo(estado,None,None,1)
    nodo = Nodo(estado,None,None,1)
    fronteira.append(nodo_inicial)
    nodoMenorCusto = nodo_inicial
    menorCusto=1000
    while fronteira:
        dist_haming = hamming_distance(estado.replace("_"),'')
        
       
        if nodoAtual.estado == "12345678_":
            caminho = percorreCaminho(nodoAtual)
            t2 = time.time()
            tempo = t2 - t1
            algoritmo = "astar_hamming"
            custo = len(caminho)
            printa_resultado(algoritmo,tempo,Nexpandidos,custo)
            return caminho

        """
        Expande o de menor custo + h(n)
        percorre todos os nodos na fronteira pra ver o qual
        """
        while nodo in fronteira:
            if (nodo.custo+dist_haming)<menorCusto:
                nodoAtual = nodo
                menorCusto = nodo.custo
                
        if nodoAtual.estado not in explorado:
            explorado
   


def calculaManhattan(estado):
    
    
    distanciaManhattan = 0
    
    for i,PosUnderline in enumerate(estado):
        PosUnderline = achaunderline(estado)

        x_0 = int(i/ 3)
        y_0 = i % 3
        
        x = int(PosUnderline /3)
        
        y = PosUnderline % 3
        distanciaManhattan  += abs(x_0-x) + abs(y_0 - y)
    return distanciaManhattan 




def astar_manhattan(estado):
    t1 = time.time()
    Nexpandidos = 0
    algoritmo = "A* Manhattan"
    fronteira = PriorityQueue()
    explorado = set()
    nodo_inicial = Nodo(estado,None,None,1)
    #tupla -> (nodo,custo)
    fronteira.put((nodo_inicial,0))
    
    
    
    #print(fronteira)
    
    
    while fronteira.empty() == False:     
        nodoAtual = fronteira.get()[0]
        
        
        #print(fronteira.empty())
        
        
        

        if nodoAtual.estado == "12345678_":
            
            caminho = percorreCaminho(nodoAtual)
            #print(caminho)
            t2 = time.time()
            tempo = t2 - t1
            algoritmo = "A* Manhattan"
            custo = len(caminho)
            printa_resultado(algoritmo,tempo,Nexpandidos,custo)
            return caminho

            
            
        if nodoAtual.estado not in explorado:
            explorado.add(nodoAtual.estado)
            sucessores = expande(nodoAtual)
            Nexpandidos = Nexpandidos + len(sucessores)
            for suc in sucessores:
                f = suc.custo
                g = calculaManhattan(suc.estado)
                h = f + g
                fronteira.put((suc, h))
    
    print("Não há solução no algoritmo " + algoritmo + " para o estado inicial" + estado)
    return None
			    

    




if __name__ == "__main__":
  nodo_inicial = Nodo(estado_inicial,0,0,0)
  astar_manhattan(estado_inicial)
  bfs(estado_inicial)
  dfs(estado_inicial)
  #estadofinal="12345678"
  #print(estado_inicial.replace("_",''))
  #print(hamming_distance(estado_inicial.replace("_",''),estadofinal))
  #bfs_nodes=bfs(estado_inicial)
  #dfs_nodes=dfs(estado_inicial)
  #for n in bfs_nodes:
  #  n.print_nodo()