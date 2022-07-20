# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。 
# 
#  要求时间复杂度为O(n)。 
# 
#  
# 
#  示例1: 
# 
#  输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^5 
#  -100 <= arr[i] <= 100 
#  
# 
#  注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/ 
# 
#  
# 
#  Related Topics 数组 分治 动态规划 👍 569 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # sol1 o(n), o(n)
        # n = len(nums)
        # dp = [0]*n
        # dp[0] = nums[0]
        # for i in range(1, n):
        #     if dp[i-1] >= 0:
        #         dp[i] = dp[i-1] + nums[i]
        #     else:
        #         dp[i] = nums[i]
        # return max(dp)
        # sol2 o(n), o(1)
        n = len(nums)
        ans = nums[0]
        for i in range(1, n):
            if ans < 0:
                ans = nums[i]
            else:
                ans = ans + nums[i]
            nums[i] = ans
        return max(nums)

# leetcode submit region end(Prohibit modification and deletion)
