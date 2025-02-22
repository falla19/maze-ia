import ast

def read_maze(file):

    with open(file, "r") as f:
        # Leer la primera línea y extraer dimensiones
        dim = ast.literal_eval(f.readline().strip())

        # Leer el resto del archivo y convertir cada línea en una lista de enteros
        maze = [ast.literal_eval(line.strip()) for line in f]

    return dim, maze
