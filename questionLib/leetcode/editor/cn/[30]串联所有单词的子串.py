# 给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。 
# 
#  注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "barfoothefoobarman", words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# 输出：[6,9,12]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 由小写英文字母组成 
#  1 <= words.length <= 5000 
#  1 <= words[i].length <= 30 
#  words[i] 由小写英文字母组成 
#  
#  Related Topics 哈希表 字符串 滑动窗口 👍 778 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import copy
from collections import defaultdict


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        hashkeys = defaultdict(int)
        heads, tails = set(), set()
        for w in words:
            hashkeys[w] += 1
            heads.add(w[0])
            tails.add(w[-1])
        stride = len(words[0])
        n, m = len(s), len(words)
        l, r, ans = 0, 0, []
        while r < n:
            if s[r] in heads:
                l = r
                r += stride * m
                if r > n:
                    break
                curString = s[l:r]
                # print(l, r, curString, hashkeys)
                hkeys = copy.deepcopy(hashkeys)
                ind = l if self.cutAndPair(curString, hkeys, stride) else -1
                if ind != -1:
                    ans.append(ind)
                r = l
            r += 1
        return ans

    def cutAndPair(self, string, hkeys, stride):
        n, l, r = len(string), 0, stride - 1

        while r < n:
            if (ss := string[l:r + 1]) in hkeys:
                # print(l, r, ss)
                hkeys[ss] -= 1
                l += stride
                r += stride
            else:
                return False
        for k, v in hkeys.items():
            if v != 0:
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
