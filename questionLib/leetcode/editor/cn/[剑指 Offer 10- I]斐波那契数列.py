# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下： 
# 
#  
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1. 
# 
#  斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。 
# 
#  答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 2
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 5
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 100 
#  
# 
#  Related Topics 记忆化搜索 数学 动态规划 👍 387 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# sol1 动态规划 o(n), o(1)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for i in range(n - 1):
            a, b = b, a + b
        return b % int(1e9 + 7)

# # sol2 记忆化递归 o(n), o(n)
# class Solution:
#     def fib_mem(self, n, dp) -> int:
#         if n <= 1:
#             return n
#         if dp[n] != 0:
#             return dp[n]
#         dp[n] = self.fib_mem(n-1, dp) + self.fib_mem(n-2, dp)
#         return dp[n]
#
#     def fib(self, n: int) -> int:
#         dp = [0]*101
#         return self.fib_mem(n, dp) % int(1e9+7)

# leetcode submit region end(Prohibit modification and deletion)
