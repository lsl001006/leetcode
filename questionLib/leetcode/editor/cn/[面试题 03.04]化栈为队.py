# 实现一个MyQueue类，该类用两个栈来实现一个队列。 
#  示例： MyQueue queue = new MyQueue(); queue.push(1); queue.push(2); queue.peek()
# ;  // 返回 1 queue.pop();   // 返回 1 queue.empty(); // 返回 false 说明： 
#  
#  你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size 和 is empty 操作是合法的。 
# 
#  你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。 
#  假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。 
#  
# 
#  Related Topics 栈 设计 队列 👍 57 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.que.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.que.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.que[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.que

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# leetcode submit region end(Prohibit modification and deletion)
