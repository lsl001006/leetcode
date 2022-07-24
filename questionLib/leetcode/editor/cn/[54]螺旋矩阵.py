# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
#  
#  
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 10 
#  -100 <= matrix[i][j] <= 100 
#  
# 
#  Related Topics 数组 矩阵 模拟 👍 1151 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # ans存储最终结果，i，j指示当前行进到的格子的行号和列号
        ans, i, j = [], 0, 0
        # 矩阵不为空循环
        while matrix:
            # 左上角出发，且保证矩阵不为空
            if i == j == 0 and matrix:
                # 矩阵整行加进ans
                ans += matrix[i]
                # 此时i不变，j走到最后一位，直接记为-1
                j = - 1
                # 把矩阵的这一行删除
                matrix.pop(i)
                # print(f'lt:{matrix}')
            # 右上角出发，且保证矩阵不为空
            if i == 0 and j == -1 and matrix:
                # 逐行添加最右一位数字到ans,并将其从matrix的该行中删除
                for r in range(len(matrix)):
                    ans.append(matrix[r].pop(j))
                # 特别注意，若matrix单行仅有1个元素，则pop之后会变成[]而不是直接删除
                # 这将影响判断逻辑，因此如果出现matrix[i] == []时，则说明matrix已经为空，退出循环
                if not matrix[i]:
                    break
                i = -1
                # print(f'rt:{matrix}')
            # 右下，同左上理
            if i == j == -1 and matrix:
                ans += matrix[i][::-1]
                j = 0
                matrix.pop(i)
                # print(f'rb:{matrix}')
            # 左下， 同右上理
            if i == -1 and j == 0 and matrix:
                for r in range(len(matrix) - 1, -1, -1):
                    ans.append(matrix[r].pop(j))
                if not matrix[i]:
                    break
                i = 0
                # print(f'lb:{matrix}')
        return ans

# leetcode submit region end(Prohibit modification and deletion)
