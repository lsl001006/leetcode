# 整数数组 nums 按升序排列，数组中的值 互不相同 。 
# 
#  在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[
# k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2
# ,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。 
# 
#  给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。 
# 
#  你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：nums = [1], target = 0
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5000 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums 中的每个值都 独一无二 
#  题目数据保证 nums 在预先未知的某个下标上进行了旋转 
#  -10⁴ <= target <= 10⁴ 
#  
#  Related Topics 数组 二分查找 👍 2159 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        二分查找某数所在的index
        :param nums:旋转后数组
        :param target:待寻找数字
        :return: index
        0:4567012 -> 7>0 -> 0 found
        4:5670124 -> 0<7 0>1 -> find left min and right max: 5, 4 -> found
        2:5670124 -> 2<4 -> 0124 ind = 3 -> s=0, e=4, m=2 ind=3 -> 2 index = 2+3=5
        6:5670124 -> 6>5 -> 5670 ind = 0 -> s=5, e=0. m=7 ind=0 -> 567  ind=0 -> 6 index = ind+1 = 1
        2:567 -10 123 -> -1,0 -> -1<0 -1 < 7 0< 1
        2: 4567 8 9123 -> 89 1 23 -> 123 ->2
        9:4567 8 912 -> 89 1 2 ind=4 -> 891 ind=4+0 -> index=4+1
        8901 2 3456
        """
        n = len(nums)
        mid = n//2
        start = 0
        end = n-1
        while 1:
            if nums[start] == target:
                return start
            elif nums[mid] == target:
                return mid
            elif nums[end] == target:
                return end
            if start == mid or end == mid:
                return -1

            if nums[mid] < nums[start]:
                if target < nums[mid] or target > nums[start]:
                    end = mid
                    mid = (mid + start) // 2
                elif nums[mid] < target < nums[end]:
                    start = mid
                    mid = (mid + end) // 2
                else:
                    return -1
            else:
                if nums[mid] > target > nums[start]:
                    end = mid
                    mid = (mid + start) // 2
                elif target > nums[mid] or target < nums[end]:
                    start = mid
                    mid = (mid + end) // 2
                else:
                    return -1
        return -1


# leetcode submit region end(Prohibit modification and deletion)
