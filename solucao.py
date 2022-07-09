
import time
estado_inicial = "2_3541687"
lista_nodos = []
lista_esq = []
lista_dir = []
lista_abaixo = []

class Nodo:
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
    sucessores = [esquerda(Lestado,achaunderline(Lestado)), direita(Lestado,achaunderline(Lestado)),acima(Lestado,achaunderline(Lestado)),abaixo(Lestado,achaunderline(Lestado))]
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


def esquerda(Lestado,posunderline):
    mov = "esquerda"
    posicoes_sem_movimento = [0,3,6]
    auxLestado = Lestado[:]
    if posunderline in posicoes_sem_movimento:
        return None
    else:
        auxLestado[posunderline] = auxLestado[posunderline-1]
        auxLestado[posunderline-1] = "_"
        estado = "".join(auxLestado)
        return (mov,estado)
    


def direita(Lestado,posunderline):
    mov = "direita"
    posicoes_sem_movimento = [2,5,8]
    auxLestado = Lestado[:]
    if posunderline in posicoes_sem_movimento:
        return None
    else:
        auxLestado[posunderline] = auxLestado[posunderline+1]
        auxLestado[posunderline+1] = "_"
        estado = "".join(auxLestado)
        return (mov,estado)


#não sei se ta certa
def abaixo(Lestado,posunderline):
    mov = "abaixo"
    posicoes_sem_movimento = [6,7,8]
    auxLestado = Lestado[:]
    if posunderline in posicoes_sem_movimento:
        return None
    else:
        auxLestado[posunderline] = auxLestado[posunderline+3]
        auxLestado[posunderline+3] = "_"
        estado = "".join(auxLestado)
        return (mov,estado)

def acima(Lestado,posunderline):
    mov = "acima"
    posicoes_sem_movimento = [0,1,2]
    auxLestado = Lestado[:]
    if posunderline in posicoes_sem_movimento:
        return None
    else:
        auxLestado[posunderline] = auxLestado[posunderline-3]
        auxLestado[posunderline-3] = "_"
        estado = "".join(auxLestado)
        return (mov,estado)

def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

#########################################################
def bfs(estado):
    
    t1 = time.time()
    Nexpandidos = 0
    fronteira = []
    explorado = set()
    nodo_inicial = Nodo(estado,None,None,1)
    fronteira.append(nodo_inicial)
    
    
    #print(fronteira)
    
    
    while fronteira:          # Creating loop to visit each node
        nodoAtual = fronteira[0]
        fronteira.pop(0)

        if nodoAtual.estado == "12345678_":
            caminho = percorreCaminho(nodoAtual)
            #print(caminho)
            t2 = time.time()
            tempo = t2 - t1
            algoritmo = "BFS"
            custo = len(caminho)
            printa_resultado(algoritmo,tempo,Nexpandidos,custo)
            return caminho

            
            
        if nodoAtual.estado not in explorado:
            explorado.add(nodoAtual.estado)
            sucessores = expande(nodoAtual)
            Nexpandidos = Nexpandidos + len(sucessores)
            #for suc in sucessores:
            #    fronteira.append(suc)
            fronteira.extend(sucessores)
      
def dfs(estado):
    t1= time.time()
    NExpandidos = 0
    pilha = []
    expandidos = set()
    nodoAtual = Nodo(estado,None,None,1)
    expandidos.add(nodoAtual.estado)
    

    #tem que fazer a funçao de ve se tem solução ou não

    while True:
        sucessores = expande(nodoAtual)
        NExpandidos = NExpandidos + len(sucessores)


        for suc in sucessores:
            if suc.estado not in expandidos:
                pilha.append(suc)

        
        nodoAtual = pilha.pop()
        expandidos.add(nodoAtual.estado)
        

        if(nodoAtual.estado == "12345678_"):
            caminho = percorreCaminho(nodoAtual)
            #print(caminho)
            t2 = time.time()
            tempo = t2 - t1
            algoritmo = "DFS"
            custo = len(caminho)
            printa_resultado(algoritmo,tempo,NExpandidos,custo)
            return caminho
  
  
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






if __name__ == "__main__":
  nodo_inicial = Nodo(estado_inicial,0,0,0)
  estadofinal="12345678"
  print(estado_inicial.replace("_",''))
  print(hamming_distance(estado_inicial.replace("_",''),estadofinal))
  #bfs_nodes=bfs(estado_inicial)
  #dfs_nodes=dfs(estado_inicial)
  #for n in bfs_nodes:
  #  n.print_nodo()