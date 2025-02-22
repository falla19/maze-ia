import ast

def read_maze(file):

    with open(file, "r") as f:
        # Leer la primera línea y extraer dimensiones
        dim = ast.literal_eval(f.readline().strip())

        # Leer el resto del archivo y convertir cada línea en una lista de enteros
        maze = [ast.literal_eval(line.strip()) for line in f]

    return dim, maze


def maze_to_graph(maze):
    """
    Converts a maze matrix into an adjacency list graph.
    
    :param maze: 2D list representing the maze.
    :return: Dictionary where keys are (row, col) positions and values are lists of adjacent positions.
    """
    rows, cols = len(maze), len(maze[0])
    graph = {}

    # Possible moves: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] != 1:  # Ignore walls
                neighbors = []
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != 1:
                        neighbors.append((nr, nc))
                graph[(r, c)] = neighbors  # Store valid moves

    return graph
