from collections import deque
import heapq

class Grafo:

    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia # Diccionario que representa la lista de adyacencia

    def obtener_vecinos(self, v):
        return self.lista_adyacencia[v]  # Devuelve los vecinos de un nodo 'v' utilizando la lista de adyacencia

    # funcion heuristica
    def h(self, nodo_actual, nodo_final):
        '''# Asegurar que los nodos sean tuplas con coordenadas
        if not isinstance(nodo_actual, tuple) or not isinstance(nodo_final, tuple):
            raise ValueError(f"Los nodos deben ser tuplas (fila, columna), pero se recibieron: {nodo_actual}, {nodo_final}")
        '''
        # Calcula y devuelve la heurística basada en la distancia Manhattan
        # La distancia Manhattan es la suma de las diferencias absolutas de las coordenadas
        #return abs(nodo_actual[0] - nodo_objetivo[0]) + abs(nodo_actual[1] - nodo_objetivo[1])
        #return distance.chebyshev(nodo_actual, nodo_objetivo)
        return max(abs(a - b) for a, b in zip(nodo_actual, nodo_final))

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
        """
        Implementa el algoritmo de búsqueda A* para encontrar un camino en el grafo.

        param nodo_inicio: Nodo desde donde se inicia la búsqueda.
        param nodo_final: Nodo objetivo a alcanzar.
        return: Lista con el camino desde nodo_inicio hasta nodo_final si se encuentra, de lo contrario None.
        """
        open_set = []  # Lista que actúa como una cola de prioridad para los nodos por explorar
        heapq.heappush(open_set, (0, nodo_inicio, [nodo_inicio]))  # Inserta el nodo inicial en el open set con prioridad 0
        costos = {nodo_inicio: 0}  # Diccionario para almacenar los costos acumulados para llegar a cada nodo

        while open_set: # Mientras el open set tenga elementos
            _, actual, camino = heapq.heappop(open_set)  # Extrae el nodo con la menor prioridad (costo + heurística)

            if actual == nodo_final:  # Si se encuentra el nodo objetivo, retorna el camino completo
                return camino

            for vecino in self.obtener_vecinos(actual):  # Itera sobre los vecinos del nodo actual
                costo=1 # Costo de moverse a un vecino
                nuevo_costo = costos[actual] + costo  # Calcula el costo acumulado para llegar al vecino
                if vecino not in costos or nuevo_costo < costos[vecino]:  # Si se encuentra un camino más barato, se actualiza
                    costos[vecino] = nuevo_costo  # Actualiza el costo del camino más barato al vecino
                    prioridad = nuevo_costo + self.h(vecino, nodo_final)  # Calcula la prioridad del vecino para el open set
                    heapq.heappush(open_set, (prioridad, vecino, camino + [vecino]))  # Agrega el vecino al open set con su prioridad

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
    
