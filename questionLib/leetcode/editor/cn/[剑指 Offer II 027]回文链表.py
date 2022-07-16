# 给定一个链表的 头节点 head ，请判断其是否为回文链表。
# 
#  如果一个链表是回文，那么链表节点序列从前往后看和从后往前看是相同的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入: head = [1,2,3,3,2,1]
# 输出: true 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入: head = [1,2]
# 输出: false
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表 L 的长度范围为 [1, 10⁵] 
#  0 <= node.val <= 9 
#  
# 
#  
# 
#  进阶：能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
# 
#  
# 
#  注意：本题与主站 234 题相同：https://leetcode-cn.com/problems/palindrome-linked-list/ 
#  Related Topics 栈 递归 链表 双指针 👍 66 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from copy import deepcopy


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        left, right = 0, len(lst) - 1
        while left < right:
            if lst[left] != lst[right]:
                return False
            left += 1
            right -= 1
        return True
