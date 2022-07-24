# 统计一个数字在排序数组中出现的次数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2 
# 
#  示例 2: 
# 
#  
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0 
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
# 
#  
# 
#  注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-
# position-of-element-in-sorted-array/ 
# 
#  Related Topics 数组 二分查找 👍 334 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r, ans = 0, len(nums) - 1, 0
        while l <= r:
            if nums[l] > target:
                break
            if nums[r] < target:
                break
            mid = (l + r) // 2
            if nums[mid] == target:
                l = mid - 1
                r = mid + 1
                ans += 1
                while l >= 0:
                    if nums[l] == target:
                        ans += 1
                    l -= 1
                while r <= len(nums) - 1:
                    if nums[r] == target:
                        ans += 1
                    r += 1
                break
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
