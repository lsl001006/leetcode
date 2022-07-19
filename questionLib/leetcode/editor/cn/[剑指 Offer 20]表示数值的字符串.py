# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。 
# 
#  数值（按顺序）可以分成以下几个部分： 
# 
#  
#  若干空格 
#  一个 小数 或者 整数 
#  （可选）一个 'e' 或 'E' ，后面跟着一个 整数 
#  若干空格 
#  
# 
#  小数（按顺序）可以分成以下几个部分： 
# 
#  
#  （可选）一个符号字符（'+' 或 '-'） 
#  下述格式之一：
#  
#  至少一位数字，后面跟着一个点 '.' 
#  至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字 
#  一个点 '.' ，后面跟着至少一位数字 
#  
#  
#  
# 
#  整数（按顺序）可以分成以下几个部分： 
# 
#  
#  （可选）一个符号字符（'+' 或 '-'） 
#  至少一位数字 
#  
# 
#  部分数值列举如下： 
# 
#  
#  ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"] 
#  
# 
#  部分非数值列举如下： 
# 
#  
#  ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"] 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "0"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "e"
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "."
# 输出：false 
# 
#  示例 4： 
# 
#  
# 输入：s = "    .1  "
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 20 
#  s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，空格 ' ' 或者点 '.' 。 
#  
#  Related Topics 字符串 👍 359 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            {' ': 0, 's': 1, 'd': 2, '.': 4},  # 0. start with 'blank'
            {'d': 2, '.': 4},  # 1. 'sign' before 'e'
            {'d': 2, '.': 3, 'e': 5, ' ': 8},  # 2. 'digit' before 'dot'
            {'d': 3, 'e': 5, ' ': 8},  # 3. 'digit' after 'dot'
            {'d': 3},  # 4. 'digit' after 'dot' (‘blank’ before 'dot')
            {'s': 6, 'd': 7},  # 5. 'e'
            {'d': 7},  # 6. 'sign' after 'e'
            {'d': 7, ' ': 8},  # 7. 'digit' after 'e'
            {' ': 8}  # 8. end with 'blank'
        ]
        p = 0  # start with state 0
        for c in s:
            if '0' <= c <= '9':
                t = 'd'  # digit
            elif c in "+-":
                t = 's'  # sign
            elif c in "eE":
                t = 'e'  # e or E
            elif c in ". ":
                t = c  # dot, blank
            else:
                t = '?'  # unknown
            if t not in states[p]:
                return False
            p = states[p][t]
        return p in (2, 3, 7, 8)

# leetcode submit region end(Prohibit modification and deletion)
