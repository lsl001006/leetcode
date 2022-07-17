# 给定一个非空且只包含非负数的整数数组 nums，数组的 度 的定义是指数组里任一元素出现频数的最大值。 
# 
#  你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,2,3,1]
# 输出：2
# 解释：
# 输入数组的度是 2 ，因为元素 1 和 2 的出现频数最大，均为 2 。
# 连续子数组里面拥有相同度的有如下所示：
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组 [2, 2] 的长度为 2 ，所以返回 2 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,2,3,1,4,2]
# 输出：6
# 解释：
# 数组的度是 3 ，因为元素 2 重复出现 3 次。
# 所以 [2,2,3,1,4,2] 是最短子数组，因此返回 6 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums.length 在 1 到 50,000 范围内。 
#  nums[i] 是一个在 0 到 49,999 范围内的整数。 
#  
#  Related Topics 数组 哈希表 👍 419 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def findRange(self, arr, k):
        head, tail = 0, len(arr) - 1
        while True:
            if arr[head] == k:
                break
            head += 1
        while True:
            if arr[tail] == k:
                break
            tail -= 1
        return [head, tail]

    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        d = {}
        sortedKeys = sorted(cnt.keys(), key=lambda x: cnt[x], reverse=True)
        maxd = cnt[sortedKeys[0]]
        mind = 50001
        for k in sortedKeys:
            if cnt[k] == maxd:
                l = self.findRange(nums, k)
                mind = min(l[1] - l[0] + 1, mind)
            else:
                break
        return mind

# leetcode submit region end(Prohibit modification and deletion)
