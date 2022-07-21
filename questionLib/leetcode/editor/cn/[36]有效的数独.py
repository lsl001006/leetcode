# 请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。 
# 
#  
#  数字 1-9 在每一行只能出现一次。 
#  数字 1-9 在每一列只能出现一次。 
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图） 
#  
# 
#  
# 
#  注意： 
# 
#  
#  一个有效的数独（部分已被填充）不一定是可解的。 
#  只需要根据以上规则，验证已经填入的数字是否有效即可。 
#  空白格用 '.' 表示。 
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# 输出：false
# 解释：除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无
# 效的。 
# 
#  
# 
#  提示： 
# 
#  
#  board.length == 9 
#  board[i].length == 9 
#  board[i][j] 是一位数字（1-9）或者 '.' 
#  
# 
#  Related Topics 数组 哈希表 矩阵 👍 921 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def isValid(self, flatList):
        cnt = Counter("".join(flatList))
        for k, v in cnt.items():
            if k != '.' and v > 1:
                return False
        return True

    def isValidSudoku(self, board) -> bool:
        border = [[0, 3], [3, 6], [6, 9]]
        # 1.遍历每一行
        for i in range(9):
            if not self.isValid(board[i]):
                return False
        # 2. 遍历每一列, 注意不能采取类似numpy的索引方式board[:][j]
        for j in range(9):
            tmp = [board[i][j] for i in range(9)]
            if not self.isValid(tmp):
                return False
        # 3. 遍历每一宫
        for i in border:
            for j in border:
                Gong = board[i[0]:i[1]]
                flatGong = [Gong[m][n] for m in range(3) for n in range(j[0], j[1])]
                # print(flatGong)
                if not self.isValid(flatGong):
                    return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
