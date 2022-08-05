# 在给定的 m x n 网格
#  grid 中，每个单元格可以有以下三个值之一： 
# 
#  
#  值 0 代表空单元格； 
#  值 1 代表新鲜橘子； 
#  值 2 代表腐烂的橘子。 
#  
# 
#  每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。 
# 
#  返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
#  
# 
#  示例 3： 
# 
#  
# 输入：grid = [[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 10 
#  grid[i][j] 仅为 0、1 或 2 
#  
# 
#  Related Topics 广度优先搜索 数组 矩阵 👍 581 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchFresh(self, grid, path, i, j):
        m, n = len(grid), len(grid[0])
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n:
                if grid[x][y] == 1:
                    grid[x][y] = 2
                    path[x * n + y] = 2
        grid[i][j] = -1
        path[i * n + j] = -1
        return grid, path

    def orangesRotting(self, grid) -> int:
        time, m, n = 0, len(grid), len(grid[0])
        path = [grid[i][j] for i in range(m) for j in range(n)]
        if path.count(1) < 1:
            return time
        while path.count(2) > 0:
            stack = []
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        stack.append([i, j])
            while stack:
                i, j = stack.pop()
                grid, path = self.searchFresh(grid, path, i, j)
            time += 1
            print(grid)
        return time - 1 if path.count(1) == 0 else -1

# leetcode submit region end(Prohibit modification and deletion)
