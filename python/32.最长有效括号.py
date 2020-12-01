#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:



# @lc code=end
from input import InputString

def main():
    s = InputString.customInputString()
    print(Solution().longestValidParentheses(s))


if __name__ == "__main__":
    main()
