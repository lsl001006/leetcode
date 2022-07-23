# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。 
# 
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。 
# 
#  问总共有多少条不同的路径？ 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：m = 3, n = 7
# 输出：28 
# 
#  示例 2： 
# 
#  
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下
#  
# 
#  示例 3： 
# 
#  
# 输入：m = 7, n = 3
# 输出：28
#  
# 
#  示例 4： 
# 
#  
# 输入：m = 3, n = 3
# 输出：6 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= m, n <= 100 
#  题目数据保证答案小于等于 2 * 10⁹ 
#  
# 
#  Related Topics 数学 动态规划 组合数学 👍 1468 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 初始化dp数组
        # 问题分解：走到每一个格子需要dp[i][j]步
        # 状态转移方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # 解释：走到当前位置的方式(dp[i][j])是走到全部相邻位置方式(dp[i-1][j], dp[i][j-1])之和
        #      由于机器人只能向下或者向右，则只有左侧(dp[i][j-1])和上侧(dp[i-1][j])两个相邻已到达位置
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 注意，由于机器人尽可以向下或向右走，因此左边和上边仅有1种到达方式
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

# leetcode submit region end(Prohibit modification and deletion)
