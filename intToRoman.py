class Solution:
    def intToRoman(self, num: int) -> str:
        ROMAN = [(1000, "M"),
                 (900, "CM"),
                 (500, "D"),
                 (400, "CD"),
                 (100, "C"),
                 (90, "XC"),
                 (50, "L"),
                 (40, "XL"),
                 (10, "X"),
                 (9, "IX"),
                 (5, "V"),
                 (4, "IV"),
                 (1, "I")]
        res = ''
        while num > 0:
            for val, char in ROMAN:
                if num >= val:
                    num -= val
                    res += char
                    break
        return res


def main():
    # leetcode functions
    result = Solution().intToRoman(3)
    print(result)


if __name__ == '__main__':
    main()
