#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
from typing import List
# @lc code=start

# f(i,j) = min(f(i-1,j)+grid[i][j],f(i,j-1)+grid[i][j])


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if (not grid or not grid[0]):
            return 0
        row = len(grid)  # row 行
        col = len(grid[0])  # col 列
        dp = [[0] * col for _ in range(row)]
        dp[0][0] = grid[0][0]
        for i in range(1, row):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, col):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, row):
            for j in range(1, col):
               dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[row - 1][col - 1]


# @lc code=end
