# 从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，
# 可以看成任意数字。A 不能视为 14。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: [1,2,3,4,5]
# 输出: True 
# 
#  
# 
#  示例 2: 
# 
#  
# 输入: [0,0,1,2,5]
# 输出: True 
# 
#  
# 
#  限制： 
# 
#  数组长度为 5 
# 
#  数组的数取值为 [0, 13] . 
# 
#  Related Topics 数组 排序 👍 256 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        kings = 0
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                kings += 1
            else:
                if (k := nums[i + 1] - nums[i] - 1) == -1 or k > kings:
                    return False
                else:
                    kings -= k
        return True

# leetcode submit region end(Prohibit modification and deletion)
