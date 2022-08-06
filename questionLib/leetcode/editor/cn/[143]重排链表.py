# 给定一个单链表 L 的头节点 head ，单链表 L 表示为： 
# 
#  
# L0 → L1 → … → Ln - 1 → Ln
#  
# 
#  请将其重新排列后变为： 
# 
#  
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → … 
# 
#  不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3] 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3] 
# 
#  
# 
#  提示： 
# 
#  
#  链表的长度范围为 [1, 5 * 10⁴] 
#  1 <= node.val <= 1000 
#  
# 
#  Related Topics 栈 递归 链表 双指针 👍 981 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseNode(self, node):
        if not node:
            return
        prev, cur = None, node
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return
        prev = ListNode(0)
        prev.next = head
        fast, slow = head, prev
        # 快慢指针找到中点
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 断链！
        second = slow.next
        slow.next = None
        # 反转second链表！
        second = self.reverseNode(second)
        first = head
        cur = first
        while cur:
            tmp = cur.next
            # 寻找反转链表第一位（原来的最后一位）并断链
            last = second
            second = second.next
            # last的下一位指向tmp
            last.next = tmp
            # cur接上last,cur移到tmp的位置
            cur.next = last
            pre_cur = last
            cur = last.next
        # 若存在未拼接完成的second列表,则接到pre_cur(倒数第一个节点)之后
        if second:
            pre_cur.next = second

# leetcode submit region end(Prohibit modification and deletion)
