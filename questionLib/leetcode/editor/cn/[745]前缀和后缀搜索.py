# 设计一个包含一些单词的特殊词典，并能够通过前缀和后缀来检索单词。 
# 
#  实现 WordFilter 类： 
# 
#  
#  WordFilter(string[] words) 使用词典中的单词 words 初始化对象。 
#  f(string pref, string suff) 返回词典中具有前缀 prefix 和后缀 suff 的单词的下标。如果存在不止一个满足要求的下标，
# 返回其中 最大的下标 。如果不存在这样的单词，返回 -1 。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# 输出
# [null, 0]
# 解释
# WordFilter wordFilter = new WordFilter(["apple"]);
# wordFilter.f("a", "e"); // 返回 0 ，因为下标为 0 的单词：前缀 prefix = "a" 且 后缀 suff = "e" 。
# 
#  
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 10⁴ 
#  1 <= words[i].length <= 7 
#  1 <= pref.length, suff.length <= 7 
#  words[i]、pref 和 suff 仅由小写英文字母组成 
#  最多对函数 f 执行 10⁴ 次调用 
#  
#  Related Topics 设计 字典树 字符串 👍 139 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class WordFilter:
    # # sol1 暴力解法
    # def __init__(self, words: List[str]):
    #     self.d = {}
    #     for i, word in enumerate(words):
    #         m = len(word)
    #         for prefixLength in range(1, m + 1):
    #             for suffixLength in range(1, m + 1):
    #                 self.d[word[:prefixLength] + '#' + word[-suffixLength:]] = i
    #
    # def f(self, pref: str, suff: str) -> int:
    #     return self.d.get(pref + '#' + suff, -1)

    # sol2 字典树解法

    def __init__(self, words: List[str]):
        self.trie = {}
        self.weightKey = ('#', '#')
        for i, word in enumerate(words):
            cur = self.trie
            m = len(word)
            for j in range(m):
                tmp = cur
                for k in range(j, m):
                    key = (word[k], '#')
                    if key not in tmp:
                        tmp[key] = {}
                    tmp = tmp[key]
                    tmp[self.weightKey] = i
                tmp = cur
                for k in range(j, m):
                    key = ('#', word[-k - 1])
                    if key not in tmp:
                        tmp[key] = {}
                    tmp = tmp[key]
                    tmp[self.weightKey] = i
                key = (word[j], word[-j - 1])
                if key not in cur:
                    cur[key] = {}
                cur = cur[key]
                cur[self.weightKey] = i

    def f(self, pref: str, suff: str) -> int:
        cur = self.trie
        for key in zip_longest(pref, suff[::-1], fillvalue='#'):
            if key not in cur:
                return -1
            cur = cur[key]
        return cur[self.weightKey]

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
# leetcode submit region end(Prohibit modification and deletion)
