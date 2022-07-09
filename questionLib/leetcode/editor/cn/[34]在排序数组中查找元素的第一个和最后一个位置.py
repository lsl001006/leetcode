# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。 
# 
#  如果数组中不存在目标值 target，返回 [-1, -1]。 
# 
#  你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1] 
# 
#  示例 3： 
# 
#  
# 输入：nums = [], target = 0
# 输出：[-1,-1] 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  nums 是一个非递减数组 
#  -10⁹ <= target <= 10⁹ 
#  
#  Related Topics 数组 二分查找 👍 1770 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """

        :param nums:
        :param target:
        :return:
        11222 2 22334
        1: s=0, 112 2 22 -> 11 2 2 -> 1 1 2 e=1 -> s=0,e=1
        2: -> 112 2 22 -> 11 2 2 -> 22 s=2 -> 222 3 34 -> 22 2 3 -> 222 e=7 -> s=2,e=7
        3: 222 3 34 -> 334 s=8 -> 33 e=9 -> s=8,e=9
        """
        if not nums:
            return [-1,-1]
        start = 0
        end = len(nums)-1
        mid = (start+end)//2
        if target > end or target < start:
            return [-1,-1]
        tar_start = -1
        tar_end = -1
        # 首先把特殊情况排除
        if nums[mid - 1] == nums[mid + 1] and nums[mid] == target:

        while start < end:
            if nums[start] == target:
                tar_start = start
            if nums[end] == target:
                tar_end = end




# leetcode submit region end(Prohibit modification and deletion)
