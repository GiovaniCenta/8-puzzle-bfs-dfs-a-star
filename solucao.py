

estado_inicial = "12345678_"
lista_nodos = []
lista_esq = []
lista_dir = []
lista_abaixo = []

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
    return [("esquerda",esquerda(estado)), ("direita",direita(estado)),("abaixo",abaixo(estado)),("acima",acima(estado))]
    


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
    
    #custo_filho = nodo.custo
    
    custo = nodo.custo


    #não sei o que fazer quando não tem mais sucessores
    
        #retirar da lista de tuplas da funcao sucessor
        
        #inicial - "2_3541687"

    suc_esq = sucessor(nodo.estado)[0]
    suc_dir = sucessor(nodo.estado)[1]
    suc_abaixo = sucessor(nodo.estado)[2]
    suc_acima = sucessor(nodo.estado)[3]
        
        #criar os nodos que seram colocados na lista de nodos sucessores
    esquerda = Nodo(suc_esq[1],nodo,suc_esq[0],custo+1)
    abaixo = Nodo(suc_abaixo[1],nodo,suc_abaixo[0],custo+1)
    direita = Nodo(suc_dir[1],nodo,suc_dir[0],custo+1)
    acima = Nodo(suc_acima[1],nodo,suc_acima[0],custo+1)
            
        

  

        
        #colocar na lista
    lista_nodos.append(esquerda)
    lista_nodos.append(direita)
    lista_nodos.append(abaixo)
    lista_nodos.append(acima)
    
        
        

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

     1  procedure BFS(G, root) is
 2      let Q be a queue
 3      label root as explored
 4      Q.enqueue(root)
 5      while Q is not empty do
 6          v := Q.dequeue()
 7          if v is the goal then
 8              return v
 9          for all edges from v to w in G.adjacentEdges(v) do
10              if w is not labeled as explored then
11                  label w as explored
12                  Q.enqueue(w)
    
    """
    # substituir a linha abaixo pelo seu codigo

    import queue

    fila = queue.Queue()
  
    visitado = []
    

    nodo_inicial = Nodo(estado,0,0,0)
    fila.put(nodo_inicial)
    
    visitado.append(nodo_inicial)
    #print(fila)
    
    
    while fila:          # Creating loop to visit each node
        v = fila.get()
        print(v.estado)
        if v.estado == "_12345678":
            return visitado
            
        else:
          
          lista_sucessores = expande(v)
          
          for sucessor in reversed(lista_sucessores):
              if sucessor not in visitado:
                  visitado.append(sucessor)
                  fila.put(sucessor)
        
            
        
        
        
        
        
    print(visitado)
    




def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:


    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
  
  procedure DFS_iterative(G, v) is
    let S be a stack
    S.push(v)
    while S is not empty do
        v = S.pop()
        if v is not labeled as discovered then
            label v as discovered
            for all edges from v to w in G.adjacentEdges(v) do 
                S.push(w)

"""
    S = []
    visitados = []
    nodo_inicial = Nodo(estado,0,0,0)
    S.append(nodo_inicial)
    while S:
        v = S.pop()
        print(v.estado)
        if v not in visitados:
            visitados.append(v)
            lista_sucessores = expande(v)
        
        for sucessor in reversed(lista_sucessores):
          S.append(sucessor)
      
  
  
  
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
    if(i == 0 or i == 3 or i == 6):  #nessas posições não vai mais para esquerda
        estado = ''.join(estado)
        return str(estado)
        
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
    if(i == 2 or i == 5 or i == 8):
        estado = ''.join(estado)
        return str(estado)
        
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
    if(i == 6 or i == 7 or i == 8):
        estado = ''.join(estado)
        return str(estado)
    else:
        estado = list(estado)
        aux = estado[i]
        aux2 = estado[i+3]
        estado[i] = aux2
        estado[i+3] = aux
        estado = ''.join(estado)
        return str(estado)

def acima(estado):
    i = estado.find("_")
    if(i == 0 or i == 1 or i == 2):
        estado = ''.join(estado)
        return str(estado)
    else:
        estado = list(estado)
        aux = estado[i]
        aux2 = estado[i-3]
        estado[i] = aux2
        estado[i-3] = aux
        estado = ''.join(estado)
        return str(estado)


if __name__ == "__main__":
  nodo_inicial = Nodo(estado_inicial,0,0,0)
  bfs_nodes=bfs(estado_inicial)
  for n in bfs_nodes:
    n.print_nodo()