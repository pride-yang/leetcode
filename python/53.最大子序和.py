#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
from typing import List
# @lc code=start


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        maxNum = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            if maxNum < dp[i]:
                maxNum = dp[i]
        return maxNum


# @lc code=end

from input import InputNums


def main():
    s = InputNums.main()
    max = Solution().maxSubArray(s)
    print(max)


if __name__ == "__main__":
    main()
