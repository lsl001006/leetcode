# 现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 
# prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。 
# 
#  
#  例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。 
#  
# 
#  返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：[0,1]
# 解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# 输出：[0,2,1,3]
# 解释：总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
# 因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。 
# 
#  示例 3： 
# 
#  
# 输入：numCourses = 1, prerequisites = []
# 输出：[0]
#  
# 
#  
# 提示：
# 
#  
#  1 <= numCourses <= 2000 
#  0 <= prerequisites.length <= numCourses * (numCourses - 1) 
#  prerequisites[i].length == 2 
#  0 <= ai, bi < numCourses 
#  ai != bi 
#  所有[ai, bi] 互不相同 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序 👍 674 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int 课程门数
        :type prerequisites: List[List[int]] 课程与课程之间的关系
        :rtype: bool
        """
        # 课程的长度
        clen = len(prerequisites)
        if clen == 0:
            # 没有课程，当然可以完成课程的学习
            return [i for i in range(numCourses)]
        # 入度数组，一开始全部为 0
        in_degrees = [0 for _ in range(numCourses)]
        # 邻接表
        adj = [set() for _ in range(numCourses)]
        # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
        # 1 -> 0，这里要注意：不要弄反了
        for second, first in prerequisites:
            in_degrees[second] += 1
            adj[first].add(second)

        # print("in_degrees", in_degrees)
        # 首先遍历一遍，把所有入度为 0 的结点加入队列
        res = []
        queue = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        while queue:
            top = queue.pop(0)
            res.append(top)

            for successor in adj[top]:
                in_degrees[successor] -= 1
                if in_degrees[successor] == 0:
                    queue.append(successor)
        if len(res) != numCourses:
            return []
        return res


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    s = Solution().findOrder(numCourses, prerequisites)

# leetcode submit region end(Prohibit modification and deletion)
