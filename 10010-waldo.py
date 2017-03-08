import sys


def diagonals(L):
    h, w = len(L), len(L[0])
    return [[L[h - p + q - 1][q]
             for q in range(max(p - h + 1, 0), min(p + 1, w))]
            for p in range(h + w - 1)]


def antidiagonals(L):
    h, w = len(L), len(L[0])
    return [[L[p - q][q]
             for q in range(max(p - h + 1, 0), min(p + 1, w))]
            for p in range(h + w - 1)]


if __name__ == '__main__':
    cases = sys.stdin.readline()
    for i in range(int(cases)):
        sys.stdin.readline()
        lineas, columnas = sys.stdin.readline().strip().split(" ")
        list_lines = []

        for linea in range(int(lineas)):
            list_lines.append(list(sys.stdin.readline().strip().lower()))
        words = sys.stdin.readline().strip()

        list_words = []

        for word in range(int(words)):
            list_words.append(list(sys.stdin.readline().strip().lower()))

        list_column = []

        for column in range(int(columnas)):
            s = []
            for linea in range(int(lineas)):
                s.append(list_lines[linea][column])
            list_column.append(s)

        list_diag = diagonals(list_lines)
        list_antidiag = antidiagonals(list_lines)

        for word in list_words:
            reverse_word = word[::-1]
            flag = False

            numLinea = 1
            for line in list_lines:
                pos = ''.join(line).find(''.join(word))
                reverse_pos = ''.join(line).rfind(''.join(reverse_word))
                if pos != -1:
                    print(str(numLinea) + " " + str(pos + 1))
                    flag = True
                    break
                elif reverse_pos != -1:
                    print(str(numLinea) + " " + str(reverse_pos + 1))
                    flag = True
                    break
                numLinea += 1

            if not flag:
                numLinea = 1
                for line in list_column:
                    pos = ''.join(line).find(''.join(word))
                    reverse_pos = ''.join(line).rfind(''.join(reverse_word))
                    if pos != -1:
                        print(str(pos + 1) + " " + str(numLinea))
                        flag = True
                        break
                    elif reverse_pos != -1:
                        print(str(reverse_pos + 1) + " " + str(numLinea))
                        flag = True
                        break
                    numLinea += 1
            if not flag:
                numLinea = 1
                for line in list_diag:
                    pos = ''.join(line).find(''.join(word))
                    reverse_pos = ''.join(line).rfind(''.join(reverse_word))
                    if pos != -1:
                        print(str((pos % int(lineas)) + 1) + " " + str(numLinea+1))
                        flag = True
                        break
                    elif reverse_pos != -1:
                        print(str((reverse_pos % int(lineas)) + 1) + " " + str(numLinea+1))
                        flag = True
                        break
                    numLinea += 1
            if not flag:
                numLinea = 1
                for line in list_antidiag:
                    pos = ''.join(line).find(''.join(word))
                    reverse_pos = ''.join(line).rfind(''.join(reverse_word))
                    if pos != -1:
                        print(list_antidiag)
                        print(line)
                        print(word)
                        print(str(numLinea) + " " + str((pos % int(lineas)) + 1))
                        flag = True
                        break
                    elif reverse_pos != -1:
                        print(list_antidiag)
                        print(line)
                        print(reverse_word)
                        print(str(numLinea) + " " + str((reverse_pos % int(lineas)) + 1))
                        flag = True
                        break
                    numLinea += 1

        print()
