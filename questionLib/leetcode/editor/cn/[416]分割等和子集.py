# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 100 
#  
# 
#  Related Topics 数组 动态规划 👍 1435 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1 or len(nums) < 2:
            return False
        target = sum(nums) // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
                if dp[-1]:
                    return True
        return dp[target]

# leetcode submit region end(Prohibit modification and deletion)
