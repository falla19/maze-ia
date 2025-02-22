from maze import read_maze, maze_to_graph # Import the function from maze.py
from grafo import Grafo # Import the function from maze.py

# Load the maze
def print_maze(maze, dim):
    # Print results
    print(f"Dimensions: {dim}")

    for row in matrix:
        print(row)

def solve_maze():
    dim, matrix = read_maze("data/laberinto.txt")
    adj_list = maze_to_graph(matrix)
    graph = Grafo(adj_list)
    print(graph.lista_adyacencia)

if __name__ == "__main__":
    solve_maze()
