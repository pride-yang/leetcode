#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        strLength = len(s)
        dp = [[False] * strLength for _ in range(strLength)]
        ans = ""
        for l in range(strLength):
            for i in range(strLength):
                j = l + i
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans


# @lc code=end
from input import *


def main():
    x = customInputString()
    print(x)
    print(Solution().longestPalindrome(x))


if __name__ == "__main__":
    main()