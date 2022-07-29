# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#  
# 
#  示例 2： 
#  
#  
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 5 * 10⁴] 内 
#  -10⁵ <= Node.val <= 10⁵ 
#  
# 
#  
# 
#  进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？ 
# 
#  Related Topics 链表 双指针 分治 排序 归并排序 👍 1724 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # sol1 递归法归并排序 O(nlogn), O(n)
        # if not head:
        #     return None
        # if not head.next:
        #     return head
        # # 归并排序第一步，cut:
        # # 利用快慢指针找到链表中点
        # fast, slow = head.next, head
        # while fast and fast.next:
        #     fast, slow = fast.next.next, slow.next
        # # mid保留中点后面的链，slow.next = None则将前半段cut下来
        # mid, slow.next = slow.next, None
        # # 递归处理
        # left, right = self.sortList(head), self.sortList(mid)
        # # 归并排序第二步：merge：
        # head = ListNode(0)
        # res = head
        # while left and right:
        #     if left.val < right.val:
        #         head.next, left = left, left.next
        #     else:
        #         head.next, right = right, right.next
        #     head = head.next
        # head.next = left if left else right
        # return res.next

        # sol2 自底而上式非递归解法 O(nlogn), O(1)
        h, length, intv = head, 0, 1
        while h: h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        # merge the list in different intv.
        while intv < length:
            pre, h = res, res.next
            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                if i:
                    break  # no need to merge because the `h2` is None.
                h2, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                c1, c2 = intv, intv - i  # the `c2`: length of `h2` can be small than the `intv`.
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            intv *= 2
        return res.next

# leetcode submit region end(Prohibit modification and deletion)
