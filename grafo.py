from collections import deque

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
        """
        Implementa el algoritmo de búsqueda en profundidad para encontrar un camino en el grafo.
    
        param nodo_inicio: Nodo desde donde se inicia la búsqueda.
        param nodo_final: Nodo objetivo a alcanzar.
        return: Lista con el camino desde nodo_inicio hasta nodo_final si se encuentra, de lo contrario None.
        """
        visited = [] # Lista para almacenar los nodos visitados
        stack = [nodo_inicio] # Pila para controlar la exploración de nodos
        parent={} # Diccionario para almacenar el nodo padre de cada nodo visitado
        while stack: # Mientras la pila tenga elementos

            s=stack.pop() # Extrae el último nodo de la pila (LIFO)
            if s == nodo_final: # Se encontró el nodo objetivo
                path=[] # Lista para almacenar el camino
                while s in parent: # Reconstrucción del camino desde el nodo objetivo hasta el inicio
                   path.append(s) # Agrega el nodo actual al camino
                   s = parent[s] # Se mueve al nodo padre
                path.append(nodo_inicio) # Agrega el nodo inicial al camino
                path.reverse() # Se invierte el camino para mostrarlo en orden correcto
                return path  # Retorna el camino encontrado
            
            if s not in visited: # Verifica que el nodo no haya sido visitado
                visited.append(s) # Marca el nodo como visitado

                if s in self.lista_adyacencia: # Verifica que el nodo tenga vecinos
                   for vecino in self.obtener_vecinos(s): # Agrega los vecinos del nodo a la pila
                    if vecino not in visited: # Verifica que el vecino no haya sido visitado
                       parent[vecino] = s # Guarda el nodo actual como padre del vecino
                       stack.append(vecino) # Agrega el vecino a la pila
        return None
        
    def primero_anchura(self, start, goal): # Busqueda en anchura
        """
        Implements Breadth-First Search (BFS) to find the shortest path from start to goal.
        
        :param start: Starting node (row, col).
        :param goal: Goal node (row, col).
        :return: List representing the shortest path from start to goal, or None if no path found.
        """
        queue = deque([start]) # Cola para explorar los nodos en orden de anchura
        visited = {start: None} # Diccionario para almacenar los nodos visitados y su nodo padre

        while queue: # Mientras la cola tenga elementos
            node = queue.popleft() # Extrae el primer nodo de la cola (FIFO)

            if node == goal: # Se encontró el nodo objetivo
                return self.reconstruct_path(visited, start, goal) # Reconstruye el camino desde el inicio hasta el objetivo

            for neighbor in self.obtener_vecinos(node): # Recorre los vecinos del nodo actual
                if neighbor not in visited: # Verifica que el vecino no haya sido visitado
                    visited[neighbor] = node # Guarda el nodo actual como padre del vecino
                    queue.append(neighbor) # Agrega el vecino a la cola

        return None  # No path found
    
    # funcion para reconstruir el camino
    def reconstruct_path(self, visited, start, goal): 
        """
        Reconstructs the path from start to goal using the visited dictionary.
        """
        path = [] # Lista para almacenar el camino
        current = goal # Inicia desde el nodo objetivo
        while current: # Mientras haya nodos en el camino
            path.append(current) # Agrega el nodo actual al camino
            current = visited[current] # Se mueve al nodo padre
            if current == start: # Verifica si se llegó al nodo de inicio
                path.append(start) # Agrega el nodo de inicio al camino
                break
        return path[::-1]  # Reverse the path to get start -> goal 

    
    def a_estrella(self, nodo_inicio, nodo_final):
       #inserte si codigo aqui
        return None

    
def maze_to_adj_list(maze):
    """
    Convierte una matriz de laberinto en una lista de adyacencia.

    param maze: Lista que representa el laberinto.
    return: Diccionario donde las claves son posiciones (fila, columna)
             y los valores son listas de posiciones adyacentes accesibles.
    """
    rows, cols = len(maze), len(maze[0]) # Obtiene el número de filas y columnas
    adj_list = {} # Diccionario que representará el grafo
    start, goal = None, None # Inicializa las posiciones de inicio y objetivo

    # Possible moves: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(rows): # Recorre cada posición del laberinto
        for c in range(cols): # Recorre cada posición del laberinto
            if maze[r][c] != 1: # Verifica que la posición no sea una pared
                # Identificar la posición inicial (2) y la meta (3)
                if maze[r][c] == 2: 
                    start = (r, c)  # Identify start position
                elif maze[r][c] == 3: 
                    goal = (r, c)  # Identify goal position

                neighbors = [] # Lista de vecinos accesibles
                for dr, dc in directions: # Evaluar las cuatro direcciones posibles
                    nr, nc = r + dr, c + dc # Nueva posición
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != 1: # Verificar límites y no sea pared
                        neighbors.append((nr, nc)) # Agregar vecino válido
                adj_list[(r, c)] = neighbors  # Store valid moves

    return adj_list, start, goal
    
