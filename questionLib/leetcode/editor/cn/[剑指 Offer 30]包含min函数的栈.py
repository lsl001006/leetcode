# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。 
# 
#  
# 
#  示例: 
# 
#  MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.min();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.min();   --> 返回 -2.
#  
# 
#  
# 
#  提示： 
# 
#  
#  各函数的调用总次数不超过 20000 次 
#  
# 
#  
# 
#  注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/ 
#  Related Topics 栈 设计 👍 364 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstk = [2 << 31]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.minstk.append(min(x, self.minstk[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minstk.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.minstk[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
# leetcode submit region end(Prohibit modification and deletion)
