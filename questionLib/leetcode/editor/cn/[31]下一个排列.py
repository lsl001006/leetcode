# 整数数组的一个 排列 就是将其所有成员以序列或线性顺序排列。 
# 
#  
#  例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。 
#  
# 
#  整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就
# 是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。 
# 
#  
#  例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。 
#  类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。 
#  而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。 
#  
# 
#  给你一个整数数组 nums ，找出 nums 的下一个排列。 
# 
#  必须 原地 修改，只允许使用额外常数空间。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[1,3,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,1]
# 输出：[1,2,3]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,1,5]
# 输出：[1,5,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 100 
#  
#  Related Topics 数组 双指针 👍 1769 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        214653 -> 215346 : 46532 -> 56432 -> 52346 643->
        21453 -> 21534 : 453 -> sort 345 -> 5 34
        1324 -> 1342 : 24 -> 42
        4321 -> 1234 : 4321 -> sort 1234
        215346 -> 215364
        思路：
        首先从nums的最后一位开始寻找，找到第一个打破倒序增长的index: e.g. 12543 则index=1
        然后倒序寻找第一个比nums[index]大的数
        """
        end = len(nums) - 1
        tmpMax = 0
        break_point = 0
        flg = 0
        while end >= 0:
            if nums[end] < tmpMax:
                break_point = nums[end]
                flg = 1
                break
            else:
                tmpMax = nums[end]
            end -= 1
        if flg == 0:
            start = 0
            stop = len(nums) - 1
            while start < stop:
                nums[start], nums[stop] = nums[stop], nums[start]
                start += 1
                stop -= 1
        else:
            for i in range(len(nums) - 1, end, -1):
                if break_point < nums[i]:
                    nums[i], nums[end] = nums[end], nums[i]
                    break

            start = end + 1
            stop = len(nums) - 1
            while start < stop:
                nums[start], nums[stop] = nums[stop], nums[start]
                start += 1
                stop -= 1

    # def switch_inplace(self, nums, start, end):
    #     """
    #     inplace的元素交换
    #     :param nums:
    #     :param start:
    #     :param end:
    #     :return:
    #     """
    #     while start < end:
    #         nums[start], nums[end] = nums[end], nums[start]
    #         start += 1
    #         end -= 1
    #     return nums

# leetcode submit region end(Prohibit modification and deletion)
