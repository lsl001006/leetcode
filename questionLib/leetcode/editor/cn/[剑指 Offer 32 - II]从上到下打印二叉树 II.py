# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。 
# 
#  
# 
#  例如: 
# 给定二叉树: [3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层次遍历结果： 
# 
#  [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
# 
#  
# 
#  提示： 
# 
#  
#  节点总数 <= 1000 
#  
# 
#  注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-
# traversal/ 
#  Related Topics 树 广度优先搜索 二叉树 👍 236 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que = [root]
        orders = [[root.val]]
        while True:
            children = []
            level = []
            for node in que:
                if node.left:
                    children.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    children.append(node.right)
                    level.append(node.right.val)
            if not children:
                break
            orders.append(level)
            que = children
        return orders

# leetcode submit region end(Prohibit modification and deletion)
