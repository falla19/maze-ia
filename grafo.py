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
        
    def primero_anchura(self, start, goal):
        """
        Implements Breadth-First Search (BFS) to find the shortest path from start to goal.
        
        :param start: Starting node (row, col).
        :param goal: Goal node (row, col).
        :return: List representing the shortest path from start to goal, or None if no path found.
        """
        queue = deque([start])
        visited = {start: None}

        while queue:
            node = queue.popleft()

            if node == goal:
                return self.reconstruct_path(visited, start, goal)

            for neighbor in self.obtener_vecinos(node):
                if neighbor not in visited:
                    visited[neighbor] = node
                    queue.append(neighbor)

        return None  # No path found

    def reconstruct_path(self, visited, start, goal):
        """
        Reconstructs the path from start to goal using the visited dictionary.
        """
        path = []
        current = goal
        while current:
            path.append(current)
            current = visited[current]
            if current == start:
                path.append(start)
                break
        return path[::-1]  # Reverse the path to get start -> goal

    
    def a_estrella(self, nodo_inicio, nodo_final):
       #inserte si codigo aqui
        return None

    
def maze_to_adj_list(maze):
    """
    Converts a maze matrix into an adjacency list.
    
    :param maze: 2D list representing the maze.
    :return: Dictionary where keys are (row, col) positions and values are lists of adjacent positions.
    """
    rows, cols = len(maze), len(maze[0])
    adj_list = {}
    start, goal = None, None

    # Possible moves: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] != 1: # Ignore walls

                if maze[r][c] == 2:
                    start = (r, c)  # Identify start position
                elif maze[r][c] == 3:
                    goal = (r, c)  # Identify goal position

                neighbors = []
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != 1:
                        neighbors.append((nr, nc))
                adj_list[(r, c)] = neighbors  # Store valid moves

    return adj_list, start, goal
    
