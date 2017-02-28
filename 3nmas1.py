import sys


def algorithm(n):
    count = 1
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    return count


def exercise(i, j):
    n1 = min(i, j)
    n2 = max(i, j)
    result = 0
    for k in range(n1, n2 + 1):
        if results.get(k):
            result = max(results.get(k), result)
        else:
            new = algorithm(k)
            results[k] = new
            result = max(new, result)
    return result


if __name__ == '__main__':
    final = ""
    results = {}
    for lin in sys.stdin:
        lin = lin.rstrip('\n')
        if len(lin.split()) < 2:
            i = int(lin.split()[0])
            j = i
        else:
            i = int(lin.split()[0])
            j = int(lin.split()[1])
        final += str(i) + ' ' + str(j) + ' ' + str(exercise(i, j)) + '\n'
    final = final[0:len(final) - 1]
    print(final)
