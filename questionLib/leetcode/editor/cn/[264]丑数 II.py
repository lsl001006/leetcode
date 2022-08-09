# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。 
# 
#  丑数 就是只包含质因数 2、3 和/或 5 的正整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 1690 
#  
# 
#  Related Topics 哈希表 数学 动态规划 堆（优先队列） 👍 947 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nthUglyNumber(self, n):
        if n < 0:
            return 0
        dp = [1] * n
        index2, index3, index5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(2 * dp[index2], 3 * dp[index3], 5 * dp[index5])
            if dp[i] == 2 * dp[index2]: index2 += 1
            if dp[i] == 3 * dp[index3]: index3 += 1
            if dp[i] == 5 * dp[index5]: index5 += 1
        return dp[n - 1]

# leetcode submit region end(Prohibit modification and deletion)
