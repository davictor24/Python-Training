cells = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]] 
start = 13
end = 4
solutions = []

def iterate(path, row, column):
    if check(path, row, column):
        path.append(cells[row][column])
        iterate(path[:], row - 1, column)
        iterate(path[:], row + 1, column)
        iterate(path[:], row, column - 1)
        iterate(path[:], row, column + 1)
        if confirmSoln(path):
            solutions.append(path)

def check(path, row, column):
    if ((row >= 0) and (row < len(cells)) and
        (column >= 0) and (column < len(cells[0]))):
        if ((path.count(cells[row][column]) == 0) or (cells[row][column] == start)):
            return True
    return False

def confirmSoln(path):
    return (len(set(path)) == (len(cells) * len(cells[0]))) and (path[0] == start) and (path[-1] == end)

c = [row for row in cells if start in row][0]
iterate([], cells.index(c), c.index(start))

print("There are " + str(len(solutions)) + " solutions.\n")
for solution in solutions:
    print(solution)
