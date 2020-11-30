#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
import sys
import io
import json
from typing import List
# @lc code=start


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * len(triangle+1)
              for _ in range(len(triangle[0])+1)]
        print(dp)
        for i in range(len(triangle)-2,-1,-1):
            for j in range(i+1):
                dp[i][j] = min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]

        return dp[0][0]


# @lc code=end


def stringToInt2dArray(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys

    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            triangle = stringToInt2dArray(line)

            ret = Solution().minimumTotal(triangle)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()