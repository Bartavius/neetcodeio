'''
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).
'''

def numIslands(grid) -> int:

    row, col = 0, 0
    islands = 0
    stack=[]
    seen_positions=set()

    def bounds(r, c):
        return r < len(grid) and 0 <= r and c < len(grid[0]) and 0 <= c  

    def not_seen(r, c):
        return (r, c) not in seen_positions

    def cond(r, c):
        return bounds(r, c) and not_seen(r, c)      


    while row < len(grid):
        print(row, col)
        if col >= len(grid[0]):
            col = 0
            if bounds(row + 1, col):
                row += 1
            else:
                break
        
        # if seen before, add one to column
        if (row, col) not in seen_positions and grid[row][col] == "1":
            stack = [(row, col)]
            print("found")
            islands += 1

        seen_positions.add((row, col))
        col += 1

        while stack:
            node = stack.pop()
            row = node[0]
            col = node[1]
            if cond(row-1, col) and grid[row-1][col] == "1":
                stack.append((row-1, col))
                seen_positions.add((row-1, col))
            if cond(row, col-1) and grid[row][col-1] == "1":
                stack.append((row, col-1))
                seen_positions.add((row, col-1))
            if cond(row+1, col) and grid[row+1][col] == "1":
                stack.append((row+1, col))
                seen_positions.add((row+1, col))
            if cond(row, col+1) and grid[row][col+1] == "1":
                stack.append((row, col+1))
                seen_positions.add((row, col+1))

    return islands
