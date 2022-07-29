# 给你一个字符串数组 words 。words 中每个元素都是一个包含 两个 小写英文字母的单词。 
# 
#  请你从 words 中选择一些元素并按 任意顺序 连接它们，并得到一个 尽可能长的回文串 。每个元素 至多 只能使用一次。 
# 
#  请你返回你能得到的最长回文串的 长度 。如果没办法得到任何一个回文串，请你返回 0 。 
# 
#  回文串 指的是从前往后和从后往前读一样的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  输入：words = ["lc","cl","gg"]
# 输出：6
# 解释：一个最长的回文串为 "lc" + "gg" + "cl" = "lcggcl" ，长度为 6 。
# "clgglc" 是另一个可以得到的最长回文串。
#  
# 
#  示例 2： 
# 
#  输入：words = ["ab","ty","yt","lc","cl","ab"]
# 输出：8
# 解释：最长回文串是 "ty" + "lc" + "cl" + "yt" = "tylcclyt" ，长度为 8 。
# "lcyttycl" 是另一个可以得到的最长回文串。
#  
# 
#  示例 3： 
# 
#  输入：words = ["cc","ll","xx"]
# 输出：2
# 解释：最长回文串是 "cc" ，长度为 2 。
# "ll" 是另一个可以得到的最长回文串。"xx" 也是。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 10⁵ 
#  words[i].length == 2 
#  words[i] 仅包含小写英文字母。 
#  
# 
#  Related Topics 贪心 数组 哈希表 字符串 计数 👍 20 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = Counter(words)  # 单词出现次数
        res = 0  # 最长回文串长度
        mid = False  # 是否含有中心单词
        for word, cnt in freq.items():
            # 遍历出现的单词，并更新长度
            rev = word[::-1]  # 反转后的单词
            if word == rev:
                if cnt % 2 == 1:
                    mid = True
                res += 2 * (cnt // 2 * 2)
            elif word > rev:  # 避免重复遍历
                res += 4 * min(freq[word], freq[rev])
        if mid:
            # 含有中心单词，更新长度
            res += 2
        return res

# leetcode submit region end(Prohibit modification and deletion)
