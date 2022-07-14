# 请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。 
# 
#  
# 
#  举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。 
# 
#  如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。 
# 
#  如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,
# null,null,null,null,9,8]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root1 = [1,2,3], root2 = [1,3,2]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  给定的两棵树结点数在 [1, 200] 范围内 
#  给定的两棵树上的值在 [0, 200] 范围内 
#  
#  Related Topics 树 深度优先搜索 二叉树 👍 191 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # sol1 普通递归解法
    def findLeafs(self, root, leafs):
        if not root:
            return
        if not root.left and not root.right:
            leafs.append(root.val)
        self.findLeafs(root.left, leafs)
        self.findLeafs(root.right, leafs)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1, leafs2 = [], []
        self.findLeafs(root1, leafs1)
        self.findLeafs(root2, leafs2)
        return leafs1 == leafs2
    # # sol2 编码校验解法（有概率冲突，不完备,性能一般）
    # def __init__(self):
    #     self.c1 = 0
    #     self.c2 = 0
    #
    # def findLeafs(self, root, c):
    #     if not root:
    #         return
    #     if not root.left and not root.right:
    #         if c:
    #             self.c1 += 1117
    #             self.c1 ^= root.val
    #         else:
    #             self.c2 += 1117
    #             self.c2 ^= root.val
    #     self.findLeafs(root.left, c)
    #     self.findLeafs(root.right, c)
    #
    # def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    #     self.findLeafs(root1, 0)
    #     self.findLeafs(root2, 1)
    #     return self.c1 == self.c2

# leetcode submit region end(Prohibit modification and deletion)
