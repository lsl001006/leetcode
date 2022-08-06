# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [10,5,2,6], k = 100
# 输出：8
# 解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3], k = 0
# 输出：0 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  1 <= nums[i] <= 1000 
#  0 <= k <= 10⁶ 
#  
# 
#  Related Topics 数组 滑动窗口 👍 578 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        n, ans = len(nums), 0
        left, right = 0, 0
        prod = 1
        # 滑动窗口实际使用了快慢指针，快指针（右指针）负责探索，慢指针（左指针）负责使窗口满足限定条件
        # 滑动窗口时先滑动右指针，当不满足条件时，在循环内滑动左指针直至满足条件
        while right < n:
            prod *= nums[right]
            while (left <= right) and prod >= k:
                prod //= nums[left]
                left += 1
            # 核心：直接利用数学方法计算[left,right]范围内有多少个子数组
            ans += right - left + 1
            # 右指针继续向右滑动
            right += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
