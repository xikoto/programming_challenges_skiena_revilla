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
        lineas = int(lineas)
        columnas = int(columnas)
        list_lines = []

        for linea in range(lineas):
            list_lines.append(list(sys.stdin.readline().strip().lower()))
        words = sys.stdin.readline().strip()

        list_words = []

        for word in range(int(words)):
            list_words.append(list(sys.stdin.readline().strip().lower()))

        list_column = []

        for column in range(columnas):
            s = []
            for linea in range(lineas):
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
                for line in list_diag[:columnas]:
                    pos = ''.join(line).find(''.join(word))
                    reverse_pos = ''.join(line).rfind(''.join(reverse_word))
                    if pos != -1:
                        print(str(lineas - pos) + " " + str(pos + 1))
                        flag = True
                        break
                    elif reverse_pos != -1:
                        print(str(lineas - reverse_pos) + " " + str(pos + 1))
                        flag = True
                        break
                    numLinea += 1

                    #falta hallar la posición de la linea
                if not flag:
                    cont_algo = 1
                    for line in list_diag[columnas:]:
                        pos = ''.join(line).find(''.join(word))
                        reverse_pos = ''.join(line).rfind(''.join(reverse_word))
                        if pos != -1:
                            print(str(numLinea - (pos + 1)) + " " + str(pos + columnas - len(line) + 1))
                            flag = True
                            break
                        elif reverse_pos != -1:
                            print(str(numLinea - (reverse_pos + 1)) + " " + str(reverse_pos + columnas - len(line) + 1))
                            flag = True
                            break
                        cont_algo += 1

            if not flag:
                numLinea = 1

                for line in list_antidiag[:lineas]:
                    pos = ''.join(line).find(''.join(word))
                    reverse_pos = ''.join(line).rfind(''.join(reverse_word))
                    if pos != -1:
                        print(str(numLinea - pos) + " " + str(pos + 1))
                        flag = True
                        break
                    elif reverse_pos != -1:
                        print(str(numLinea - reverse_pos) + " " + str(reverse_pos + 1))
                        flag = True
                        break
                    numLinea += 1

                if not flag:

                    cont_column = 1
                    for line in list_antidiag[lineas:]:
                        pos = ''.join(line).find(''.join(word))
                        reverse_pos = ''.join(line).rfind(''.join(reverse_word))
                        if pos != -1:
                            print(str(numLinea - (pos + 1)) + " " + str(cont_column + 1))
                            flag = True
                            break
                        elif reverse_pos != -1:
                            print(str(numLinea - (reverse_pos + 1)) + " " + str(cont_column + 1))
                            flag = True
                            break
                        cont_column += 1

        print()
