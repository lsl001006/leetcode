# 集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有
# 一个数字重复 。 
# 
#  给定一个数组 nums 代表了集合 S 发生错误后的结果。 
# 
#  请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,2,4]
# 输出：[2,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,1]
# 输出：[1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 10⁴ 
#  1 <= nums[i] <= 10⁴ 
#  
#  Related Topics 位运算 数组 哈希表 排序 👍 274 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        err = -1
        for k, v in cnt.items():
            if v == 2:
                err = k
        arr = sorted(list(cnt.keys()))
        for i in range(1, len(arr) + 1):
            if i != arr[i - 1]:
                return [err, i]
        return [err, len(arr) + 1]

# leetcode submit region end(Prohibit modification and deletion)
