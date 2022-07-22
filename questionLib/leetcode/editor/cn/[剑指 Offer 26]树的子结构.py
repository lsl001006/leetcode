# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构) 
# 
#  B是A的子结构， 即 A中有出现和B相同的结构和节点值。 
# 
#  例如: 给定的树 A: 
# 
#  3 / \ 4 5 / \ 1 2 给定的树 B： 
# 
#  4 / 1 返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。 
# 
#  示例 1： 
# 
#  输入：A = [1,2,3], B = [3,1]
# 输出：false
#  
# 
#  示例 2： 
# 
#  输入：A = [3,4,5,1,2], B = [4,1]
# 输出：true 
# 
#  限制： 
# 
#  0 <= 节点个数 <= 10000 
# 
#  Related Topics 树 深度优先搜索 二叉树 👍 598 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sameStructure(self, A, B):
        # 若把B搜索了一个遍，则返回True
        if not B:
            return True
        # 若B还没搜索完，但是A以及到头了，返回False
        if not A:
            return False
        # 若A,B均不为None,若两节点值不相等，则返回False
        if A.val != B.val:
            return False
        # 递归寻找左子树和右子树是否相同
        return self.sameStructure(A.left, B.left) and \
               self.sameStructure(A.right, B.right)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        if A.val == B.val:
            # 遇到A和B在该节点相等，则检查是否为相同结构
            same = self.sameStructure(A, B)
            if same:
                # 若相同则直接返回True
                # 若不同，则继续搜索，直至搜索完成
                return same
        L = self.isSubStructure(A.left, B)
        R = self.isSubStructure(A.right, B)
        # B只要是左右子树其中之一的子结构就可以返回True
        return L or R
# leetcode submit region end(Prohibit modification and deletion)
