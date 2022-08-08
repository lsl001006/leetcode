# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。 
# 
#  实现 MinStack 类: 
# 
#  
#  MinStack() 初始化堆栈对象。 
#  void push(int val) 将元素val推入堆栈。 
#  void pop() 删除堆栈顶部的元素。 
#  int top() 获取堆栈顶部的元素。 
#  int getMin() 获取堆栈中的最小元素。 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# 输出：
# [null,null,null,null,-3,null,0,-2]
# 
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#  
# 
#  
# 
#  提示： 
# 
#  
#  -2³¹ <= val <= 2³¹ - 1 
#  pop、top 和 getMin 操作总是在 非空栈 上调用 
#  push, pop, top, and getMin最多被调用 3 * 10⁴ 次 
#  
# 
#  Related Topics 栈 设计 👍 1373 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.quene = []
        self.minval = []

    def push(self, val: int) -> None:
        self.quene.append(val)
        if self.minval != []:
            tmp = self.minval[-1]
            if tmp < val:
                self.minval.append(tmp)
            else:
                self.minval.append(val)
        else:
            self.minval.append(val)

    def pop(self) -> None:
        self.quene.pop(-1)
        self.minval.pop(-1)

    def top(self) -> int:
        return self.quene[-1]

    def getMin(self) -> int:
        return self.minval[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)
