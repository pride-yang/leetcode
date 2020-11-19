import sys
import io
sys.path.append('../')


def customInputNum() -> int:
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = int(line)
            return s
        except StopIteration:
            break
if __name__=="__main__":
    customInputNum()