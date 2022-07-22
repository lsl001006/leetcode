# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。 
# 
#  示例 1: 
# 
#  
# 输入：s = "abaccdeff"
# 输出：'b'
#  
# 
#  示例 2: 
# 
#  
# 输入：s = "" 
# 输出：' '
#  
# 
#  
# 
#  限制： 
# 
#  0 <= s 的长度 <= 50000 
# 
#  Related Topics 队列 哈希表 字符串 计数 👍 249 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> str:
        freq = Counter(s)
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return s[i]
        return ' '

# leetcode submit region end(Prohibit modification and deletion)
