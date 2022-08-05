# 有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。 
# 
#  这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c) 上
# 单元格 高于海平面的高度 。 
# 
#  岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。 
# 
#  返回网格坐标 result 的 2D 列表 ，其中 result[i] = [ri, ci] 表示雨水从单元格 (ri, ci) 流动 既可流向太平洋也可
# 流向大西洋 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# 输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
#  
# 
#  示例 2： 
# 
#  
# 输入: heights = [[2,1],[1,2]]
# 输出: [[0,0],[0,1],[1,0],[1,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == heights.length 
#  n == heights[r].length 
#  1 <= m, n <= 200 
#  0 <= heights[r][c] <= 10⁵ 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 👍 502 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dfs(self, heights, i, j, path):
        m, n = len(heights), len(heights[0])
        path[i][j] = 1
        for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if 0 <= x < m and 0 <= y < n and path[x][y] == 0 and heights[x][y] >= heights[i][j]:
                path = self.dfs(heights, x, y, path)
        return path

    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        result = []
        Pmat = [[0 for j in range(n)] for i in range(m)]
        Amat = [[0 for j in range(n)] for i in range(m)]
        for j in range(n):
            Pmat = self.dfs(heights, 0, j, Pmat)
            Amat = self.dfs(heights, m - 1, j, Amat)
        for i in range(m):
            Pmat = self.dfs(heights, i, 0, Pmat)
            Amat = self.dfs(heights, i, n - 1, Amat)

        for i in range(m):
            for j in range(n):
                if Pmat[i][j] == Amat[i][j] == 1:
                    result.append([i, j])
        return result

# leetcode submit region end(Prohibit modification and deletion)
