# 给定一个经过编码的字符串，返回它解码后的字符串。 
# 
#  编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。 
# 
#  你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。 
# 
#  此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 30 
#  
#  s 由小写英文字母、数字和方括号
#  '[]' 组成 
#  s 保证是一个 有效 的输入。 
#  s 中所有整数的取值范围为
#  [1, 300] 
#  
# 
#  Related Topics 栈 递归 字符串 👍 1229 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def pureAlpha(self, s):
        for ch in s:
            if ch.isdigit():
                return False
        return True

    def decodeString(self, s: str) -> str:
        if self.pureAlpha(s):
            return s
        prev, end = '', ''
        # 搜集前缀
        for i in range(len(s)):
            if s[i].isdigit():
                break
            prev += s[i]
        # 更新s为去掉前缀的s
        s = s[len(prev):]
        # 搜集后缀
        for i in range(len(s) - 1, 0, -1):
            if s[i] == ']':
                break
            end = s[i] + end
        if len(end) > 0:
            s = s[:-len(end)]
        # 给并排编码分隔开
        mulstk = ['']  # 乘数栈
        arrstk = []  # 字符栈
        signstk = []  # 括号栈
        tmparr = ''
        for i in range(len(s)):
            # 符号栈为空且为数字字符时
            if signstk == [] and s[i].isdigit():
                if tmparr != '':
                    mulstk[-1] = '1'
                    mulstk.append('')
                    arrstk.append(tmparr)
                    tmparr = ''
                mulstk[-1] += s[i]
                continue

            if s[i] == '[':
                # 若符号栈不为空
                if signstk:
                    tmparr += '['
                else:
                    mulstk.append('')
                signstk.append(s[i])
                continue

            if s[i] == ']':
                if len(signstk) > 1:
                    signstk.pop()
                    tmparr += ']'
                else:
                    signstk.pop()  # 此刻栈应被清空
                    arrstk.append(tmparr)  # 括号里的全部字符写入完成，加入arrstk
                    tmparr = ''  # 清空临时字符串
                continue
            # 进行到此处，仅有括号里的数字与字母
            tmparr += s[i]

        fullstr = prev
        for i in range(len(arrstk)):
            fullstr += int(mulstk[i]) * self.decodeString(arrstk[i])
        fullstr += end
        return fullstr

# leetcode submit region end(Prohibit modification and deletion)
