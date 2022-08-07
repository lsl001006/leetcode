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
        # cnter字典中是否所有的键对应的值都小于等于零
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
        # 随意初始化一个len(s)长度的结果字符串
        res = '0' * len(s)
        # 使用快慢指针进行滑动窗口
        left, right, n = 0, 0, len(s)
        # right快指针用于探索，寻找整体上包含t中所有字符的大致字符串
        while right < n:
            # right指针每寻找到一个t中的字符（也就是t_cnter的key）,t_cnter[key] -= 1
            if (c := s[right]) in t_cnter:
                t_cnter[c] -= 1
            # 当t_cnter中所有的键对应的值都被清零，说明我们找到了一个包含t所有字符的子串
            # 接下来我们需要利用left指针在该子串的基础上，找到包含t中所有字符的最小子串
            if self.allClear(t_cnter):
                # 1.当left指针指向的不是所需字符 或 2.left指针指向的所需字符出现多次时：
                # 对于2情况，可以假设right指针找到包含‘ABC’的字符串'DDAABBDC'
                # 我们需要找到的包含'ABC'的最小子串为'ABBDC'，而不是'AABBDC'
                # t_cnter初始值为{'A':1,'B':1,'C':1}, 而由right指针找到第一个令
                # t_cnter中每个键值小于等于0的字符串是‘DDAABBDC',此时t_cnter= {'A':-1,'B':-1,'C':0}
                # 也就是此时我们查到的字符串包含多个A,B,我们希望的子串可以尽可能地短
                # 因此我们需要找到字符串左侧第一个使t_cnter[s[left]]恰好满足条件的字符位置
                # 这里的我们希望的最小子串左端为A,我们希望以最后一个恰好满足条件的A出现在子串左侧，使得子串最短
                while (s[left] not in t_cnter) or t_cnter[s[left]] < 0:
                    if s[left] in t_cnter:
                        t_cnter[s[left]] += 1
                    left += 1
                # 若子串比现有子串长度短，则更新res
                if right - left + 1 <= len(res):
                    res = s[left:right + 1]
                # s[left]是当前子串最左侧的字母，必属于t_cnter.keys()
                # left右移一位，使得t_cnter恰好不满足条件，触发right指针继续寻找新的子串
                t_cnter[s[left]] += 1
                left += 1
            right += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
