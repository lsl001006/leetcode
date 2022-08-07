# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。 
# 
#  
# 
#  注意： 
# 
#  
#  对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。 
#  如果 s 中存在这样的子串，我们保证它是唯一的答案。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a", t = "a"
# 输出："a"
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 10⁵ 
#  s 和 t 由英文字母组成 
#  
# 
#  
# 进阶：你能设计一个在 
# o(n) 时间内解决此问题的算法吗？
# 
#  Related Topics 哈希表 字符串 滑动窗口 👍 2050 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def allClear(self, cnter):
        for k, v in cnter.items():
            if v > 0:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        t_cnter = Counter(t)
        s_cnter = Counter(s)
        # 验证存在性
        for k, v in t_cnter.items():
            if k not in s_cnter or s_cnter[k] < v:
                return ''
        res = '0' * len(s)
        tmp_cnter = t_cnter
        left, right, n = 0, 0, len(s)
        while right < n:
            if (c := s[right]) in tmp_cnter:
                tmp_cnter[c] -= 1
            if self.allClear(tmp_cnter):
                while (s[left] not in tmp_cnter) or tmp_cnter[s[left]] < 0:
                    if s[left] in tmp_cnter:
                        tmp_cnter[s[left]] += 1
                    left += 1

                if right - left + 1 <= len(res):
                    res = s[left:right + 1]
                tmp_cnter[s[left]] += 1
                left += 1
            right += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
