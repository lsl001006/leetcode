# 给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。 
# 
#  在执行上述操作后，返回包含相同字母的最长子字符串的长度。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ABAB", k = 2
# 输出：4
# 解释：用两个'A'替换为两个'B',反之亦然。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "AABABBA", k = 1
# 输出：4
# 解释：
# 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
# 子串 "BBBB" 有最长重复字母, 答案为 4。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s 仅由大写英文字母组成 
#  0 <= k <= s.length 
#  
# 
#  Related Topics 哈希表 字符串 滑动窗口 👍 655 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        ans, n = 0, len(s)
        counter = Counter()
        # 当右指针未走到右边界时循环
        while right < n:
            counter[s[right]] += 1
            while ((right + 1 - left) - counter.most_common()[0][1]) > k:
                counter[s[left]] -= 1
                left += 1
            # 寻找到了满足条件的区间
            # 记录最大长度
            ans = max(ans, (right + 1 - left))
            # 探索新的区间
            right += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
