# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。 
# 
#  
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL 
# 
#  
# 
#  限制： 
# 
#  0 <= 节点个数 <= 5000 
# 
#  
# 
#  注意：本题与主站 206 题相同：https://leetcode-cn.com/problems/reverse-linked-list/ 
#  Related Topics 递归 链表 👍 459 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # #  sol1 暴力解法
        # if not head:
        #     return None
        # tmp = []
        # while head:
        #     tmp.append(ListNode(head.val))
        #     head = head.next
        # ans = ListNode(0)
        # start = ans
        # for i in range(len(tmp)-1, -1, -1):
        #     ans.next = tmp[i]
        #     ans = ans.next
        # return start.next

        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

# leetcode submit region end(Prohibit modification and deletion)
