import json
import sys
import io
from typing import List

def stringToIntegerList(input):
    return json.loads(input)


def customInputNums() -> List[int]:
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line)
            return nums
        except StopIteration:
            break


if __name__ == '__main__':
    customInputNums()