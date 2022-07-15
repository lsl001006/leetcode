# 实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。 示例 1: 给定二叉树 [3,9,20,
# null,null,15,7]     3    / \   9  20     /  \    15   7 返回 true 。示例 2: 给定二叉树 [1,2,
# 2,3,3,null,null,4,4]       1      / \     2   2    / \   3   3  / \ 4   4 返回 
# false 。 Related Topics 树 深度优先搜索 二叉树 👍 88 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDepth(self, root):
        if not root:
            return 0
        return max(self.findDepth(root.left), self.findDepth(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        L = self.findDepth(root.left)
        R = self.findDepth(root.right)
        if abs(L - R) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
# leetcode submit region end(Prohibit modification and deletion)
