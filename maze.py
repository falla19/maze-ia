import matplotlib.pyplot as plt
import numpy as np
import ast

from matplotlib import pyplot as plt
#Abre archivo de texto y lee la primera linea para obtener las dimensiones y 
# luego lee el resto para  convertirlo en matriz 
def read_maze(file):

    with open(file, "r") as f:
        # Leer la primera línea y extraer las dimensiones del laberinto
        dim = ast.literal_eval(f.readline().strip())

        # Leer el resto del archivo y convertir cada línea en una lista de enteros
        # Cada línea representa una fila del laberinto
        maze = [list(map(int, ast.literal_eval(line.strip()))) for line in f]  # ✅ Conversión a int

    return dim, maze

'''
# Convierte la matriz del laberinto en un grafo donde cada celda transitable (no es una pared) se convierte en un nodo.
# Define conexiones entre celdas adyacentes si no hay paredes.
def maze_to_graph(maze):
    """
    Converts a maze matrix into an adjacency list graph.
    
    :param maze: 2D list representing the maze.
    :return: Dictionary where keys are (row, col) positions and values are lists of adjacent positions.
    """
    rows, cols = len(maze), len(maze[0])  # Obtener el número de filas y columnas
    graph = {} # Diccionario que representará el grafo

    # Possible moves: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Recorrer cada celda del laberinto
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] != 1:  # Recorrer cada celda del laberinto
                neighbors = []  # Lista de vecinos accesibles
                # Evaluar las cuatro direcciones posibles
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Verificar que la nueva posición esté dentro de los límites y no sea una pared
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != 1:
                        neighbors.append((nr, nc)) # Agregar vecino válido
                graph[(r, c)] = neighbors  # Guardar los vecinos en el grafo

    return graph # Retornar el grafo representado como lista de adyacencia
'''

def search_nodes(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 2:
                source = (i, j)
            if maze[i][j] == 3:
                end = (i, j)
    return source, end


def draw_maze(maze, path, titulo ="Laberinto"):
    # Verificar si `maze` es un archivo y leerlo si es necesario
    if isinstance(maze, str):  
        _, maze = read_maze(maze)
    # Convertir la matriz en un array de NumPy
    maze_array = np.array(maze)
    
    # Crear la figura y los ejes
    fig, ax = plt.subplots()
    
    # Definir el mapa de colores
    cmap = plt.cm.colors.ListedColormap(['white', 'black', 'yellow', 'red'])  
    bounds = [-0.5, 0.5, 1.5, 2.5, 3.5]
    norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)
    
    # Dibujar el laberinto con imshow()
    ax.imshow(maze_array, cmap=cmap, norm=norm)
    
    # Pinta el camino de la solución
    for (i, j) in path:
        ax.plot(j,i, 'o', color='green')

  
    ax.set_title(titulo)

    # Mostrar la imagen
    plt.show()

