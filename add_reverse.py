import sys

if __name__ == '__main__':
    cases = sys.stdin.readline()
    for i in range(int(cases)):
        number = sys.stdin.readline().rstrip('\n')
        reverse = number[::-1]
        number = str(int(number) + int(reverse))
        reverse = number[::-1]
        count = 1
        while number != reverse:
            number = str(int(number)+int(reverse))
            reverse = number[::-1]
            count += 1
        print(str(count)+' '+number)
