#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from typing import List
from input import InputNums

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        if len(prices) == 0:
            return 0
        minPrices = prices[0]

        for i in range(1,len(prices)):
            if minPrices > prices[i]:
                minPrices = min(minPrices, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minPrices)
        return dp[len(prices) - 1]


# @lc code=end


def main():
    x = InputNums.customInputNums()
    print(x)
    print(Solution().maxProfit(x))


if __name__ == "__main__":
    main()