class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotten = set()

        row, col = len(grid), len(grid[0])
        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    rotten.add((i,j))

                elif grid[i][j] == 1:
                    fresh += 1

        count = 0

        while rotten:
            count += 1
            temp = set()

            for (x, y) in rotten:
                for (dx, dy) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nx = x + dx
                    ny = y + dy

                    #new start point(= new fresh orange)
                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 1:
                        fresh -= 1
                        grid[nx][ny] = 2 #fresh -> rotten
                        temp.add((nx, ny))

            rotten = temp

        return max(0, count-1) if fresh == 0 else -1