import ast

#Abre archivo de texto y lee la primera linea para obtener las dimensiones y 
# luego lee el resto para  convertirlo en matriz 
def read_maze(file):

    with open(file, "r") as f:
        # Leer la primera línea y extraer las dimensiones del laberinto
        dim = ast.literal_eval(f.readline().strip())

        # Leer el resto del archivo y convertir cada línea en una lista de enteros
        # Cada línea representa una fila del laberinto
        maze = [ast.literal_eval(line.strip()) for line in f]

    return dim, maze


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
