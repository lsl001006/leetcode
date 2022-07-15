# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。 
# 
#  如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。 
# 
#  我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。 
# 
#  只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。 
# 
#  
# 
#  示例 1： 
#  
# 
#  
# 输入：root = [1,2,3,4], x = 4, y = 3
# 输出：false
#  
# 
#  示例 2： 
#  
# 
#  
# 输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
# 输出：true
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：root = [1,2,3,null,4], x = 2, y = 3
# 输出：false 
# 
#  
# 
#  提示： 
# 
#  
#  二叉树的节点数介于 2 到 100 之间。 
#  每个节点的值都是唯一的、范围为 1 到 100 的整数。 
#  
# 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 274 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        广度优先搜索
        """
        fatherX, fatherY = -1, -1
        depthX, depthY, cnt = 0, 0, 0
        flgx, flgy = 0, 0
        que = [root]
        while True:
            children = []
            cnt += 1
            for node in que:
                if node.left:
                    if node.left.val == x:
                        fatherX = node.val
                        depthX = cnt
                        flgx = 1
                    if node.left.val == y:
                        fatherY = node.val
                        depthY = cnt
                        flgy = 1
                    children.append(node.left)
                if node.right:
                    if node.right.val == x:
                        fatherX = node.val
                        depthX = cnt
                        flgx = 1
                    if node.right.val == y:
                        fatherY = node.val
                        depthY = cnt
                        flgy = 1
                    children.append(node.right)
            if flgx and flgy:
                break
            if not children:
                break
            que = children
        if flgx and flgy:
            return (depthY == depthX) and (fatherX != fatherY)
        else:
            return False
# leetcode submit region end(Prohibit modification and deletion)
