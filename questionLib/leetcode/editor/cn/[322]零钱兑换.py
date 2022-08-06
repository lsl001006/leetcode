# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。 
# 
#  计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。 
# 
#  你可以认为每种硬币的数量是无限的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1 
# 
#  示例 2： 
# 
#  
# 输入：coins = [2], amount = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：coins = [1], amount = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= coins.length <= 12 
#  1 <= coins[i] <= 2³¹ - 1 
#  0 <= amount <= 10⁴ 
#  
# 
#  Related Topics 广度优先搜索 数组 动态规划 👍 2075 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if not amount:
            return 0
        # 将减法转换为除法进行运算
        # 一旦最低位为1，则说明找到解，停止运算
        dp = 1 << amount
        res = 0
        while dp:
            tmp = 0
            res += 1
            # 每一轮运算计算一遍dp除以2**i得到的所有可能解
            for coin in coins:
                # tmp用于存储运算的中间结果
                # dp >> coin 实际上是进行除法运算：dp//2**coin
                # 使用位运算“或”来保存全部除法运算结果中的‘1’，实现批量运算
                # ps:这也是二进制移位的一个神奇之处，大家可以手动模拟一下这个过程
                tmp |= dp >> coin
            # 一旦末尾出现1，则返回结果
            if tmp & 1:
                return res
            # 将本轮运算的全部运算结果送入下一轮计算
            dp = tmp
        return -1

# leetcode submit region end(Prohibit modification and deletion)
