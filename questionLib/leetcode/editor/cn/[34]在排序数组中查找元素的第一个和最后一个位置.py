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
    def searchRange(self, nums, target):
        """
        :param nums:
        :param target:
        :return:
        """
        n = len(nums)
        ans = [-1, -1]
        # 特判条件
        # 1. nums数组长度为0
        # 2. nums[0]小于target,或nums[-1]大于target
        if not n or (nums[0] > target or nums[-1] < target):
            return ans
        if n == 1 and target == nums[0]:
            return [0, 0]
        # 定义左指针l, 右指针r 用以二分搜索
        # 定义目标指针ind, 用以记录寻找到的索引值
        l, r, ind = 0, n - 1, -1
        while l < r:
            mid = (l + r) // 2
            if nums[l] == target:
                ind = l
                break
            if nums[r] == target:
                ind = r
                break
            # 只要找到一个目标值即可退出二分搜索循环
            if nums[mid] == target:
                ind = mid
                break
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        if ind != -1:
            l, r = ind, ind
            # 从ind向左右搜索
            # 1. 若l向左搜索越界，则停止向左
            # 2. 若r向右搜索越界，则停止向右
            while True:
                if l < 0:
                    l = 0
                    break
                if nums[l] < target:
                    l += 1
                    break
                l -= 1
            while True:
                if r > n - 1:
                    r = n - 1
                    break
                if nums[r] > target:
                    r -= 1
                    break
                r += 1
            ans = [l, r]
        return ans


if __name__ == '__main__':
    s = Solution().searchRange([5, 7, 7, 8, 8, 10], 10)

# leetcode submit region end(Prohibit modification and deletion)
