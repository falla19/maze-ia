from maze import read_maze  # Import the function from maze.py

# Load the maze
dim, matrix = read_maze("data/laberinto.txt")

# Print results
print(f"Dimensions: {dim}")

for row in matrix:
    print(row)


