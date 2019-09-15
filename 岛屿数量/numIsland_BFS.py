from typing import List
from collections import deque


class Solution:
    
    def numIslands(self, grid: List[List[str]]):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)]for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                # 没有被标记过 且 是陆地（‘1’）
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    queue = deque()
                    queue.append((i, j))
                    marked[i][j] = True
                    while queue:
                        cur_x, cur_y = queue.popleft()
                        for direction in self.directions:
                            new_i = cur_x + direction[0]
                            new_j = cur_y + direction[1]
                            # 不是边界、没有被标记过、是陆地
                            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                                queue.append((new_i, new_j))
                                marked[new_i][new_j] = True
        return count
    # 方向数组：从上顺时针转
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '1']]
    solution = Solution()
    result = solution.numIslands(grid)
    print(result)
