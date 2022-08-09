# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。 
# 
#  
# 
#  示例: 
# 
#  输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。 
# 
#  说明: 
# 
#  
#  1 是丑数。 
#  n 不超过1690。 
#  
# 
#  注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/ 
# 
#  Related Topics 哈希表 数学 动态规划 堆（优先队列） 👍 367 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # def nthUglyNumber(self, n: int) -> int:
    # # sol 1 最小堆解法
    #     factors = [2, 3, 5]
    #     seen = {1}
    #     heap = [1]
    #
    #     for i in range(n - 1):
    #         curr = heapq.heappop(heap)
    #         for factor in factors:
    #             if (nxt := curr * factor) not in seen:
    #                 seen.add(nxt)
    #                 heapq.heappush(heap, nxt)
    #
    #     return heapq.heappop(heap)
    # dp解法 O(n), O(n)
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1

        return dp[n]

# leetcode submit region end(Prohibit modification and deletion)
