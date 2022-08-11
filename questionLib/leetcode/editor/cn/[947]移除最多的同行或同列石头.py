# n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。 
# 
#  如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。 
# 
#  给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。 
# 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# 输出：5
# 解释：一种移除 5 块石头的方法如下所示：
# 1. 移除石头 [2,2] ，因为它和 [2,1] 同行。
# 2. 移除石头 [2,1] ，因为它和 [0,1] 同列。
# 3. 移除石头 [1,2] ，因为它和 [1,0] 同行。
# 4. 移除石头 [1,0] ，因为它和 [0,0] 同列。
# 5. 移除石头 [0,1] ，因为它和 [0,0] 同行。
# 石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。 
# 
#  示例 2： 
# 
#  
# 输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# 输出：3
# 解释：一种移除 3 块石头的方法如下所示：
# 1. 移除石头 [2,2] ，因为它和 [2,0] 同行。
# 2. 移除石头 [2,0] ，因为它和 [0,0] 同列。
# 3. 移除石头 [0,2] ，因为它和 [0,0] 同行。
# 石头 [0,0] 和 [1,1] 不能移除，因为它们没有与另一块石头同行/列。 
# 
#  示例 3： 
# 
#  
# 输入：stones = [[0,0]]
# 输出：0
# 解释：[0,0] 是平面上唯一一块石头，所以不可以移除它。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= stones.length <= 1000 
#  0 <= xi, yi <= 10⁴ 
#  不会有两块石头放在同一个坐标点上 
#  
# 
#  Related Topics 深度优先搜索 并查集 图 👍 282 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self):
        self.father = {}

    def find(self, x):
        root = x
        # 找到真正的父根节点
        while self.father[root] is not None:
            root = self.father[root]
        # 压缩
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y

    def add(self, x):
        if x not in self.father:
            self.father[x] = None

    def remain(self):
        return sum([1 for v in self.father.values() if v is None])


class Solution:
    def removeStones(self, stones) -> int:
        uf = UnionFind()
        for i, s in enumerate(stones):
            uf.add(i)
            x1, y1 = s[0], s[1]
            for j in range(i):
                x2, y2 = stones[j][0], stones[j][1]
                if x1 == x2 or y1 == y2:
                    uf.merge(i, j)

        return len(stones) - uf.remain()

# leetcode submit region end(Prohibit modification and deletion)
