# 给定一个二维矩阵 matrix，以下类型的多个请求： 
# 
#  
#  计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1, col1) ，右下角 为 (row2, col2) 。 
#  
# 
#  实现 NumMatrix 类： 
# 
#  
#  NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化 
#  int sumRegion(int row1, int col1, int row2, int col2) 返回 左上角 (row1, col1) 、右下
# 角 (row2, col2) 所描述的子矩阵的元素 总和 。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入: 
# ["NumMatrix","sumRegion","sumRegion","sumRegion"]
# [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,
# 1,2,2],[1,2,2,4]]
# 输出: 
# [null, 8, 11, 12]
# 
# 解释:
# NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,
# 0,1,7],[1,0,3,0,5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和)
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 200
#  
#  -10⁵ <= matrix[i][j] <= 10⁵ 
#  0 <= row1 <= row2 < m 
#  0 <= col1 <= col2 < n 
#  
#  最多调用 10⁴ 次 sumRegion 方法 
#  
# 
#  Related Topics 设计 数组 矩阵 前缀和 👍 420 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        # 初始化前缀和矩阵，可以采用动态规划的方式来填充
        # 在原有矩阵的基础上左上边各加一层0，方便dp推导
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + matrix[i - 1][j - 1] - dp[i - 1][j - 1]
        # 求得的前缀和矩阵dp赋予self._sum
        self._sum = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 求以[r1,c1,r2,c2]为对角坐标的矩阵之和的方法为：
        # _sum[0,0,r2+1,c2+1] - _sum[0,0,r1,c2+1] - _sum[0,0,r2+1,c1] + _sum[0,0,r1,c1]
        # 注意：_sum矩阵为(m+1)*(n+1)维度的前缀和矩阵，传入的row1,...,col2参数均为matrix(m*n)原始矩阵的参数
        #      因此实际坐标比原始坐标要+1
        return self._sum[row2 + 1][col2 + 1] - self._sum[row1][col2 + 1] \
               - self._sum[row2 + 1][col1] + self._sum[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# leetcode submit region end(Prohibit modification and deletion)
