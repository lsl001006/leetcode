# 编写一个函数，检查输入的链表是否是回文的。 
# 
#  
# 
#  示例 1： 
# 
#  输入： 1->2
# 输出： false 
#  
# 
#  示例 2： 
# 
#  输入： 1->2->2->1
# 输出： true 
#  
# 
#  
# 
#  进阶： 
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
#  Related Topics 栈 递归 链表 双指针 👍 117 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        left, right = 0, len(ans) - 1
        while left < right:
            if ans[left] != ans[right]:
                return False
            left += 1
            right -= 1
        return True
# leetcode submit region end(Prohibit modification and deletion)
