#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0 or (x % 10 == 0 and x != 0)):
            return False
        reversedNumber: int = 0
        while (x > reversedNumber):
            reversedNumber = reversedNumber * 10 + x % 10
            x//=10
        return reversedNumber == x or reversedNumber/10 ==x

# @lc code=end
def stringToString(input):
    return input


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
            s = int(line)

            ret = Solution().isPalindrome(s)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()