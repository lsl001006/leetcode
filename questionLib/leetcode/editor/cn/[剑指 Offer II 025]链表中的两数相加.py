# 给定两个 非空链表 l1和 l2 来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。 
# 
#  可以假设除了数字 0 之外，这两个数字都不会以零开头。 
# 
#  
# 
#  示例1： 
# 
#  
# 
#  
# 输入：l1 = [7,2,4,3], l2 = [5,6,4]
# 输出：[7,8,0,7]
#  
# 
#  示例2： 
# 
#  
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[8,0,7]
#  
# 
#  示例3： 
# 
#  
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表的长度范围为 [1, 100] 
#  0 <= node.val <= 9 
#  输入数据保证链表代表的数字无前导 0 
#  
# 
#  
# 
#  进阶：如果输入链表不能修改该如何处理？换句话说，不能对列表中的节点进行翻转。 
# 
#  
# 
#  
#  注意：本题与主站 445 题相同：https://leetcode-cn.com/problems/add-two-numbers-ii/ 
# 
#  Related Topics 栈 链表 数学 👍 59 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = '', ''
        while l1:
            num1 = num1 + str(l1.val)
            l1 = l1.next
        while l2:
            num2 = num2 + str(l2.val)
            l2 = l2.next
        res = list(map(lambda x: int(x), str(int(num1) + int(num2))))
        res[-1] = ListNode(res[-1])
        for i in range(len(res) - 2, -1, -1):
            res[i] = ListNode(res[i])
            res[i].next = res[i + 1]
        return res[0]

# leetcode submit region end(Prohibit modification and deletion)
