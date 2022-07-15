# 如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。 
# 
#  只有给定的树是单值二叉树时，才返回 true；否则返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：[1,1,1,1,1,null,1]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：[2,2,2,5,2]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  给定树的节点数范围是 [1, 100]。 
#  每个节点的值都是整数，范围为 [0, 99] 。 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 165 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.num = 0

    def preOrder(self, root):
        if not root:
            return True
        if root.val != self.num:
            return False
        L = self.preOrder(root.left)
        R = self.preOrder(root.right)
        return L and R

    def isUnivalTree(self, root: TreeNode) -> bool:
        self.num = root.val
        return self.preOrder(root)

# leetcode submit region end(Prohibit modification and deletion)
