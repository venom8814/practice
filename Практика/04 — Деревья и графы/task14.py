def count_islands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    islands = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            visited[r][c] or grid[r][c] == 0):
            return
        visited[r][c] = True
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                islands += 1

    return islands


if __name__ == "__main__":
    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]

    print("Количество островов:", count_islands(grid))