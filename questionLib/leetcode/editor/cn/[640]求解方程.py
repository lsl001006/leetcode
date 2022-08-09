# 求解一个给定的方程，将x以字符串 "x=#value" 的形式返回。该方程仅包含 '+' ， '-' 操作，变量 x 和其对应系数。 
# 
#  如果方程没有解，请返回 "No solution" 。如果方程有无限解，则返回 “Infinite solutions” 。 
# 
#  如果方程中只有一个解，要保证返回值 'x' 是一个整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: equation = "x+5-3+x=6+x-2"
# 输出: "x=2"
#  
# 
#  示例 2: 
# 
#  
# 输入: equation = "x=x"
# 输出: "Infinite solutions"
#  
# 
#  示例 3: 
# 
#  
# 输入: equation = "2x=x"
# 输出: "x=0"
#  
# 
#  
# 
#  
# 
#  提示: 
# 
#  
#  3 <= equation.length <= 1000 
#  equation 只有一个 '='. 
#  equation 方程由整数组成，其绝对值在 [0, 100] 范围内，不含前导零和变量 'x' 。 
#  
# 
#  Related Topics 数学 字符串 模拟 👍 93 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calc(self, eq):
        xs, vals = 0, 0
        if eq[0] == '-':
            signs = [-1]
            eq = eq[1:]
        else:
            signs = [1]
        i, n = 0, len(eq)
        eq = list(eq)
        while i < n:
            ch = eq[i]
            if ch in ['-', '+']:
                signs.append(1 if ch == '+' else -1)
                eq[i] = ' '
            i += 1
        eq = "".join(eq)
        splited = eq.split(' ')
        for i in range(len(splited)):
            if 'x' in splited[i]:
                if len(splited[i]) > 1:
                    xs += int(splited[i][:-1]) * signs[i]
                else:
                    xs += 1 * signs[i]
            else:
                vals += signs[i] * int(splited[i])
        return xs, vals

    def solveEquation(self, equation: str) -> str:
        # split
        left_eq, right_eq = equation.split('=')
        lxs, lvals = self.calc(left_eq)
        rxs, rvals = self.calc(right_eq)
        xs = lxs - rxs
        vals = lvals - rvals
        if xs == 0 and vals == 0:
            return "Infinite solutions"
        if xs == 0 and vals != 0:
            return "No solution"
        if xs != 0 and vals == 0:
            return "x=0"
        if xs != 0 and vals != 0:
            return f"x={-vals // xs}"

# leetcode submit region end(Prohibit modification and deletion)
