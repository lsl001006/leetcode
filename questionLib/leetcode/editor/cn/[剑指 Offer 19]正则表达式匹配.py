# 请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配
# 是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。 
# 
#  示例 1: 
# 
#  输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#  
# 
#  示例 2: 
# 
#  输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#  
# 
#  示例 3: 
# 
#  输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#  
# 
#  示例 4: 
# 
#  输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#  
# 
#  示例 5: 
# 
#  输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false 
# 
#  
#  s 可能为空，且只包含从 a-z 的小写字母。 
#  p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。 
#  
# 
#  注意：本题与主站 10 题相同：https://leetcode-cn.com/problems/regular-expression-matching/
#  
# 
#  Related Topics 递归 字符串 动态规划 👍 420 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def match(charS: str, charP: str) -> bool:
            """当正则字符为‘.’，或二者字符相等时，返回True"""
            return charP == '.' or charP == charS

        # dp[i][j]表示 [正则串p的前i个字符] 能否配对成功 [目标串s的前j个字符]
        # 为了更多的cache hit，我们将逐个遍历i，即逐个读入p串的字符
        lenS, lenP = len(s), len(p)
        dp = [[False] * (lenS + 1) for _ in range(lenP + 1)]

        # 空字符配对空字符则必定成功
        dp[0][0] = True

        # 如果正则串为‘X*X*X*...’的形式，则其可配对空字符串
        for i in range(1, lenP + 1):
            if p[i - 1] == '*':
                dp[i][0] = dp[i - 2][0]

        for i in range(1, lenP + 1):
            for j in range(1, lenS + 1):

                # 如果p新读入的字符是'*'，则需要比对'*'之前的字符与s的相应字符
                if p[i - 1] == '*':

                    # 1. 如果两个字符能够配对，我们用'X'表示这个字符，有两种情况：
                    # 1.1. 不使用'X*'，即p串除去'X*'的部分可以与s串配对，即dp[i-2][j]
                    # 1.2. 使用'X*'，因为我们已经确定'X'能够与s串的字符配对，因此，
                    #      只要p串之前的某一个字符与s串的这个字符配对成功过，之后'*'这行所有
                    #      能够配对的字符都能配对成功，dp[i][j-1]
                    #      e.g. 'ab*' 只要与'abbbb...'在第三行第一列配对成功了，即'ab*'与'a'的dp[3][1]
                    #           之后对于所有'bbbbb...'，dp[3][...]都是True
                    if match(s[j - 1], p[i - 2]):
                        dp[i][j] = dp[i - 2][j] or dp[i][j - 1]

                    # 2. 如果两个字符配对不成功
                    # 2.1. 此时只有不使用'X*'一种方法能够使p,s配对，即dp[i-2][j]
                    else:
                        dp[i][j] = dp[i - 2][j]

                # 如果p新读入的不是'*'，就很简单了，只要[配对]且[二者上一个字符能够配对]就可以
                else:
                    dp[i][j] = match(s[j - 1], p[i - 1]) and dp[i - 1][j - 1]

        return dp[-1][-1]

# leetcode submit region end(Prohibit modification and deletion)
