class Grafo:

    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia

    def obtener_vecinos(self, v):
        return self.lista_adyacencia[v]

    # funcion heuristica
    def h(self, n):
        #inserte su codigo aqui
        return H[n] # puede retornar una lista con el calculo de la heuristica para cada estado

    def primero_profundidad(self, nodo_inicio, nodo_final):
        visited = []
        stack = [nodo_inicio]
        parent={}
        while stack:

            s=stack.pop()
            if s == nodo_final:
                path=[]
                while s in parent:
                   path.append(s)
                   s = parent[s]
                path.append(nodo_inicio)
                path.reverse()
                return path  # Retorna el camino encontrado
            
            if s not in visited:
                visited.append(s)

                if s in self.lista_adyacencia:
                   for vecino in self.obtener_vecinos(s):
                    if vecino not in visited:
                       parent[vecino] = s
                       stack.append(vecino)
        return None
        
    def primero_anchura(self, nodo_inicio, nodo_final):
        # falla :V
        return None
    
    def a_estrella(self, nodo_inicio, nodo_final):
       #inserte si codigo aqui
        return None
    
