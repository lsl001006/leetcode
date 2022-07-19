# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。 
# 
#  序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：target = 9
# 输出：[[2,3,4],[4,5]]
#  
# 
#  示例 2： 
# 
#  输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#  
# 
#  
# 
#  限制： 
# 
#  
#  1 <= target <= 10^5 
#  
# 
#  
# 
#  Related Topics 数学 双指针 枚举 👍 461 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findContinuousSequence(self, target: int):
        i, j, res = 1, 2, []
        while i < j:
            j = (-1 + (1 + 4 * (2 * target + i * (i - 1))) ** 0.5) / 2
            if i < j == int(j):
                res.append(list(range(i, int(j) + 1)))
            i += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
