# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
# 
#  输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  限制： 
# 
#  
#  0 <= matrix.length <= 100 
#  0 <= matrix[i].length <= 100 
#  
# 
#  注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/ 
# 
#  Related Topics 数组 矩阵 模拟 👍 433 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans, i, j = [], 0, 0
        while matrix:
            # 左上
            if i == j == 0 and matrix:
                ans += matrix[i]
                j = - 1
                matrix.pop(i)
                # print(f'lt:{matrix}')
            # 右上
            if i == 0 and j == -1 and matrix:
                for r in range(len(matrix)):
                    ans.append(matrix[r].pop(j))
                if not matrix[i]:
                    break
                i = -1
                # print(f'rt:{matrix}')
            # 右下
            if i == j == -1 and matrix:
                ans += matrix[i][::-1]
                j = 0
                matrix.pop(i)
                # print(f'rb:{matrix}')
            # 左下
            if i == -1 and j == 0 and matrix:
                for r in range(len(matrix) - 1, -1, -1):
                    ans.append(matrix[r].pop(j))
                if not matrix[i]:
                    break
                i = 0
                # print(f'lb:{matrix}')
        return ans

# leetcode submit region end(Prohibit modification and deletion)
