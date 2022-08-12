# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的每个数字在每个组合中只能使用 一次 。 
# 
#  注意：解集不能包含重复的组合。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ] 
# 
#  示例 2: 
# 
#  
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ] 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
# 
#  Related Topics 数组 回溯 👍 1067 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        res = []
        # 从小到大排序，方便剪枝
        candidates.sort()

        def dfs(begin, path, remain):
            """
            寻找剩余remain时的所有可能路径
            :param begin: 当前搜索中, 剩余候选数的最小索引
            :param path: 当前搜索记录下来的路径
            :param remain: 当前剩余求和目标大小
            :return: None 不返回值，若路径有效则直接加到外部变量res中去
            """
            # 剩余为0，则说明已经找到，将该路径添加到res
            if remain == 0:
                res.append(path[:])
                return

            for i in range(begin, size):
                # 侯选数大于剩下的目标，剪枝（大剪枝）
                if candidates[i] > remain:
                    break
                # 如果当前候选数和之前已经使用过的候选数重合，则跳过
                if i > begin and candidates[i] == candidates[i - 1]:
                    continue
                # 若候选数小于等于remain且不与之前数重合，路径中添加该候选数
                path.append(candidates[i])
                # 在余下候选数中寻找所有可能路径
                dfs(i + 1, path, remain - candidates[i])
                # 将当前候选数从path中剔除（当前候选数的所有可能已经推演完毕并赋予res），
                # 继续到下一个候选数进行循环
                path.pop()

        dfs(0, [], target)
        return res
# leetcode submit region end(Prohibit modification and deletion)
