from maze import read_maze, draw_maze #, maze_to_graph, draw_maze, search_nodes # Import the function from maze.py para leer el laberinto y convertirlo en grafo
from grafo import Grafo, maze_to_adj_list # Importamos la clase Grafo para manejar la estructura del grafo

"""
# función para imprimir el laberinto
def print_maze(maze, dim): 
#Imprimir el laberinto en la consola
print(f"Dimensions: {dim}")

for row in matrix: #Recorrer cada fila del laberinto
print(row) 
"""
# Función que carga el laberinto desde un archivo, lo convierte en un grafo
def solve_maze():
    dim, matrix = read_maze("data/laberinto.txt")  # Leer el laberinto
    adj_list, start, goal = maze_to_adj_list(matrix) # Convertir el laberinto en una lista de adyacencia 
    graph = Grafo(adj_list) # Crear un objeto Grafo con la lista de adyacencia
    
    #print(graph.lista_adyacencia) #Imprime la lista
    #start, goal = search_nodes(matrix) # Buscar los nodos de inicio y objetivo
    #path = graph.primero_profundidad(start, goal) # Buscar el camino entre los nodos de inicio
    
    caminos = { # Diccionario con los métodos de búsqueda y sus caminos
        "DFS": graph.primero_profundidad(start, goal), # Buscar el camino entre los nodos de inicio y objetivo
        "BFS": graph.primero_anchura(start, goal), # Buscar el camino más corto entre los nodos de inicio y objetivo
        "A*": graph.a_estrella(start, goal), # Buscar el camino más corto entre los nodos de inicio y objetivo
    }
    
   # Imprimir y visualizar cada camino
    for metodo, path in caminos.items(): # Recorrer el diccionario de caminos
        print(f'{metodo}: {path}') # Imprimir el método y el camino
        if path: # Si se encontró un camino
            draw_maze(matrix, path, f"Laberinto - {metodo}") # Dibujar el laberinto con el camino

if __name__ == "__main__":
    solve_maze()
