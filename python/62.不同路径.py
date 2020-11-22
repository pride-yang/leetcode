#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#


# f(i,j) = f(i-1,j)+f(i,j-1)
# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(dp)
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]
# @lc code=end
def main():
    import sys
    import io

    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            m = int(line)
            line = next(lines)
            n = int(line)

            ret = Solution().uniquePaths(m, n)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()