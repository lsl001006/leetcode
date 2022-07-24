# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出
# 这个数字。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [0,1,3]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: [0,1,2,3,4,5,6,7,9]
# 输出: 8 
# 
#  
# 
#  限制： 
# 
#  1 <= 数组长度 <= 10000 
# 
#  Related Topics 位运算 数组 哈希表 数学 二分查找 👍 290 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans, l, r = -1, 0, len(nums) - 1
        while l <= r:
            if nums[l] != l:
                ans = l
                break
            if nums[r] != r + 1:
                ans = r + 1
                break
            m = (l + r) // 2
            if nums[m] == m:
                l = m + 1
            elif nums[m] > m:
                r = m

        return ans

# leetcode submit region end(Prohibit modification and deletion)
