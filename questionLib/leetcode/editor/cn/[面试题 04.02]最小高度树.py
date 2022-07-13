# 给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。示例: 给定有序数组: [-10,-3,0,5,9], 一个可能
# 的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：           0          / \        -3 
#   9        /   /      -10  5 Related Topics 树 二叉搜索树 数组 分治 二叉树 👍 130 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 终止条件
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        if len(nums) == 2:
            rt = TreeNode(nums[1])
            lf = TreeNode(nums[0])
            rt.left = lf
            return rt
        if len(nums) == 3:
            rt = TreeNode(nums[1])
            lf = TreeNode(nums[0])
            rf = TreeNode(nums[2])
            rt.left = lf
            rt.right = rf
            return rt

        mid = len(nums) // 2
        rootNode = TreeNode(nums[mid])
        lnums = nums[:mid]
        rnums = nums[mid + 1:]
        ltree = self.sortedArrayToBST(lnums)
        rtree = self.sortedArrayToBST(rnums)
        rootNode.left = ltree
        rootNode.right = rtree
        return rootNode

# leetcode submit region end(Prohibit modification and deletion)
