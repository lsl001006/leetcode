# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,2,1]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：head = [1,2]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目在范围[1, 10⁵] 内 
#  0 <= Node.val <= 9 
#  
# 
#  
# 
#  进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
# 
#  Related Topics 栈 递归 链表 双指针 👍 1450 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        l, r = 0, len(stack) - 1
        while l < r:
            if stack[l] != stack[r]:
                return False
            l += 1
            r -= 1
        return True
# leetcode submit region end(Prohibit modification and deletion)
