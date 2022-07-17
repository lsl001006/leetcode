# 对于字符串 s 和 t，只有在 s = t + ... + t（t 自身连接 1 次或多次）时，我们才认定 “t 能除尽 s”。 
# 
#  给定两个字符串 str1 和 str2 。返回 最长字符串 x，要求满足 x 能除尽 str1 且 X 能除尽 str2 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：str1 = "ABCABC", str2 = "ABC"
# 输出："ABC"
#  
# 
#  示例 2： 
# 
#  
# 输入：str1 = "ABABAB", str2 = "ABAB"
# 输出："AB"
#  
# 
#  示例 3： 
# 
#  
# 输入：str1 = "LEET", str2 = "CODE"
# 输出：""
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= str1.length, str2.length <= 1000 
#  str1 和 str2 由大写英文字母组成 
#  
#  Related Topics 数学 字符串 👍 239 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from math import gcd


class Solution:
    # def findGcd(self, a, b):
    #     while b:
    #         a, b = b, a % b
    #     return a

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # t = self.findGcd(len(str1), len(str2))
        t = gcd(len(str1), len(str2))
        rep = str1[:t]
        if int(len(str1) / t) * rep == str1 and int(len(str2) / t) * rep == str2:
            return rep
        else:
            return ""

# leetcode submit region end(Prohibit modification and deletion)
