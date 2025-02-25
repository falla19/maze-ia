from maze import read_maze, maze_to_graph, draw_maze, search_nodes # Import the function from maze.py para leer el laberinto y convertirlo en grafo
from grafo import Grafo # Importamos la clase Grafo para manejar la estructura del grafo

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
    adj_list = maze_to_graph(matrix) # Convertir el laberinto en una lista de adyacencia 
    graph = Grafo(adj_list) # Crear un objeto Grafo con la lista de adyacencia
    #print(graph.lista_adyacencia) #Imprime la lista

    source, end = search_nodes(matrix)
    path= graph.primero_profundidad(source, end) # Buscar el camino entre los nodos de inicio
    
    tipo_recorrido = "DFS" # Tipo de recorrido
    if tipo_recorrido == "DFS":
        path = graph.primero_profundidad(source, end)
    elif tipo_recorrido == "BFS":
        path = graph.primero_anchura(source, end)
    elif tipo_recorrido == "A*":
        path = graph.a_estrella(source, end)
    else:
        path = None

    if path is not None:
        draw_maze(matrix, path, f"Laberinto - {tipo_recorrido}")

    #graph.primero_profundidad(source, end)

if __name__ == "__main__":
    solve_maze()
