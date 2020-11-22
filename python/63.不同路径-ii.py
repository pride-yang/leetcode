#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
from typing import List
# @lc code=start



class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        col, row = len(obstacleGrid[0]), len(obstacleGrid)
        values = [[0] * col for _ in range(row)]

        for i in range(col):
            if obstacleGrid[0][i] == 0:
                values[0][i] = 1
            else:
                break
        for j in range(row):
            if obstacleGrid[j][0] == 0:
                values[j][0] = 1
            else:
                break
        for j in range(1, row):
            for i in range(1, col):
                if obstacleGrid[j][i] == 1:
                    values[j][i] = 0
                else:
                    values[j][i] = values[j-1][i] + values[j][i-1]

        return values[-1][-1]

# @lc code=end
