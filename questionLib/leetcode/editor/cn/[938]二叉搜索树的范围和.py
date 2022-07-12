# 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
# 输出：32
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# 输出：23
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [1, 2 * 10⁴] 内 
#  1 <= Node.val <= 10⁵ 
#  1 <= low <= high <= 10⁵ 
#  所有 Node.val 互不相同 
#  
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 294 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return None
        self.rangeSumBST(root.left, low, high)
        if low <= (value := root.val) <= high:
            self.ans += value
        self.rangeSumBST(root.right, low, high)
        return self.ans
# leetcode submit region end(Prohibit modification and deletion)
