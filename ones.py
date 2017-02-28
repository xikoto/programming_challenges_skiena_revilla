import sys

if __name__ == '__main__':
    for line in sys.stdin:
        number = int(line)
        ones = '1'
        while int(ones)%number != 0:
            ones += '1'
        print(len(ones))
