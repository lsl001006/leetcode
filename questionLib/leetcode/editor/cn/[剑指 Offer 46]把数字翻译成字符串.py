# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可
# 能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。 
# 
#  
# 
#  示例 1: 
# 
#  输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi" 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= num < 2³¹ 
#  
# 
#  Related Topics 字符串 动态规划 👍 471 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def translateNum(self, num: int) -> int:
        # 最小问题：到第i位时有几种不同翻译
        # dp推导式:
        # dp[i] = dp[i+1] + (dp[i+2] if 第i和第i+1位组合的数字<=25 且第i位不为0 else 0)
        s = str(num)
        n = len(s)
        if n == 1:
            return 1
        elif n == 2:
            return 2 if num <= 25 and s[0] != '0' else 1

        prev = 1
        cur = 2 if int(s[-2:]) <= 25 and s[-2] != '0' else 1
        for i in range(n - 3, -1, -1):
            ss = s[i:i + 2]
            cur, prev = cur + (prev if int(ss) <= 25 and ss[0] != '0' else 0), cur
        return cur

# leetcode submit region end(Prohibit modification and deletion)
