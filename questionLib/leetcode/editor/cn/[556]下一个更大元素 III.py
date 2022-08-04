# 给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。 
# 
#  注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12
# 输出：21
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 21
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2³¹ - 1 
#  
# 
#  Related Topics 数学 双指针 字符串 👍 295 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # 整体思想：
        # 利用单调栈找到index最大的第一个非倒序递增元素k，并替换为单调栈中最小的比k大的元素u
        # 随后将u,k位置互换，并将index+1:end的所有元素升序排序，可以得到符合题意的结果
        INTMAX = 2 ** 31 - 1
        # 临时存储数组
        tmp = []
        # 初始化【递增】单调栈，将数字转化为字符列表
        stk, s = [], list(str(n))
        # 倒序寻找
        for i in range(len(s) - 1, -1, -1):
            # 当单调栈不为空且最新查询的元素s[i]小于栈顶，不满足递增时
            # 循环地将不满足条件的栈顶弹出，存入tmp数组
            # 结果：当stk重新满足单增条件或为空时，结束循环
            #      此时tmp[-1]恰为 s[i:]中最小的 比s[i]大的值
            while stk and stk[-1] > s[i]:
                tmp.append(stk.pop())
            # 若tmp不为空，则将tmp[-1]与s[i]交换
            if tmp:
                s[i], tmp[-1] = tmp[-1], s[i]
                # 将s[i+1:] 替换为按从小到大排序后的stk+tmp数组
                # 注：tmp保存了stk中弹出的元素，即stk+tmp中的所有元素为当前遍历过的所有元素
                #    但在上一步的交换中，s[i]替代了tmp[-1]的位置，为使s[i+1:]数值最小
                #    应将tmp+stk排序并替换s[i+1:]
                s[i + 1:] = sorted(tmp + stk)
                # 转换为int
                ans = int("".join(s))
                return ans if ans <= INTMAX else -1
            # tmp为空时，说明stk保持单增，向stk中添加s[i]
            stk.append(s[i])
        # 当stk全部单增时，说明该数是最大的形式，返回-1
        return -1

# leetcode submit region end(Prohibit modification and deletion)
