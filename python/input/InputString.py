import sys
import io

def stringToString(input):
    return input


def customInputString() -> str:
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line)
            return s
        except StopIteration:
            break
if __name__=="__main__":
    customInputString()