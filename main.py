from maze import read_maze, maze_to_graph # Import the function from maze.py para leer el laberinto y convertirlo en grafo
from grafo import Grafo # Importamos la clase Grafo para manejar la estructura del grafo

# Load the maze
def print_maze(maze, dim): 
    #Imprimir el laberinto en la consola
    print(f"Dimensions: {dim}")

    for row in matrix: #Recorrer cada fila del laberinto
        print(row)

# Función que carga el laberinto desde un archivo, lo convierte en un grafo y lo imprime.
def solve_maze():
    dim, matrix = read_maze("data/laberinto.txt")  # Leer el laberinto
    adj_list = maze_to_graph(matrix) # Convertir el laberinto en una lista de adyacencia 
    graph = Grafo(adj_list) # Crear un objeto Grafo con la lista de adyacencia
    print(graph.lista_adyacencia)

if __name__ == "__main__":
    solve_maze()
