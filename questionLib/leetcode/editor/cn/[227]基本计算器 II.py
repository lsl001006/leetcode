# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。 
# 
#  整数除法仅保留整数部分。 
# 
#  你可以假设给定的表达式总是有效的。所有中间结果将在 [-2³¹, 2³¹ - 1] 的范围内。 
# 
#  注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "3+2*2"
# 输出：7
#  
# 
#  示例 2： 
# 
#  
# 输入：s = " 3/2 "
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：s = " 3+5 / 2 "
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 3 * 10⁵ 
#  s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开 
#  s 表示一个 有效表达式 
#  表达式中的所有整数都是非负整数，且在范围 [0, 2³¹ - 1] 内 
#  题目数据保证答案是一个 32-bit 整数 
#  
# 
#  Related Topics 栈 数学 字符串 👍 598 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, s: str) -> int:
        s = s + '+'
        funcs = '+-*/'
        stk = []
        last_func = ''
        i, n = 0, len(s)
        tmp = ''
        while i < n:
            if s[i].isdigit():
                tmp += s[i]
            if s[i] in funcs:
                if tmp != '':
                    if not stk:
                        stk.append(int(tmp))
                    else:
                        if last_func == '*':
                            stk[-1] *= int(tmp)
                        elif last_func == '/':
                            if stk[-1] < 0 and stk[-1] % int(tmp) != 0:
                                stk[-1] = stk[-1] // int(tmp) + 1
                            else:
                                stk[-1] //= int(tmp)

                        elif last_func == '-':
                            stk.append(-int(tmp))
                        else:
                            stk.append(int(tmp))
                    last_func = s[i]
                    tmp = ''
            # print(stk)
            i += 1
        return sum(stk)

# leetcode submit region end(Prohibit modification and deletion)
