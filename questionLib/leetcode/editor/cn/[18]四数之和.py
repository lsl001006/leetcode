# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[
# b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）： 
# 
#  
#  0 <= a, b, c, d < n 
#  a、b、c 和 d 互不相同 
#  nums[a] + nums[b] + nums[c] + nums[d] == target 
#  
# 
#  你可以按 任意顺序 返回答案 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  Related Topics 数组 双指针 排序 👍 1299 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        ans = {}
        nums.sort()
        for i in range(n - 3):
            if nums[i] > target > 0:
                continue
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
            for j in range(i + 1, n - 2):
                k = nums[i] + nums[j]
                if k > target > 0:
                    continue
                if k + nums[n - 2] + nums[n - 1] < target:
                    continue
                mini_goal = target - k
                l, r = j + 1, n - 1
                while l < r:
                    tmp = nums[l] + nums[r]
                    if tmp == mini_goal:
                        hashkey = 1001 * nums[i] + 101 * nums[j] + 11 * nums[l] + nums[r]
                        ans[hashkey] = [nums[i], nums[j], nums[l], nums[r]]
                        l += 1
                    if tmp > mini_goal:
                        r -= 1
                    if tmp < mini_goal:
                        l += 1

        return list(ans.values())

# leetcode submit region end(Prohibit modification and deletion)
