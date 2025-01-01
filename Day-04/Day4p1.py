
def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_length = len(word)
    counter = 0

    def checker(x,y,dx,dy):
        for i in range(word_length):

            newX = x + i * dx
            newY = y + i * dy

            
            if not ((0 <= newX < rows) and (0 <= newY < cols)):
                return False

            if grid[newX][newY] != word[i]:
                return False
        return True
        





    directions = [
    (0, 1),   
    (1, 0),   
    (1, 1),   
    (1, -1),  
    (0, -1),  
    (-1, 0),  
    (-1, -1), 
    (-1, 1)   
]

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if checker(x,y,dx,dy):
                    counter += 1

    return counter

def load_grid():
    grid = []
    with open("input.txt", "r") as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid

grid = load_grid()
count = count_xmas(grid)
print(count)
