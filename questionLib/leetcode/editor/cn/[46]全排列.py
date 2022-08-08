# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  nums 中的所有整数 互不相同 
#  
# 
#  Related Topics 数组 回溯 👍 2155 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: list[int]) -> List[List[int]]:
        n = len(nums)
        if n <= 1:
            return [nums]
        if n == 2:
            return [nums, nums[::-1]]
        ori_nums = nums[:]
        aligns = []
        for i in range(n):
            rest = nums.pop(i)
            align = self.permute(nums)
            for j in range(len(align)):
                align[j] = [rest] + align[j]
            aligns += align
            nums = ori_nums[:]
        return aligns

# leetcode submit region end(Prohibit modification and deletion)
