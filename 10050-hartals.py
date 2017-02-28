import sys

if __name__ == '__main__':

    solucion = ""

    casos =  int(sys.stdin.readline().strip())

    for caso in range(0, casos):
        numDias = sys.stdin.readline().strip()

        if not numDias:
            break

        numPartidos = int(sys.stdin.readline().strip())

        solSet = set()
        for partido in range(0, numPartidos):
            hartal = sys.stdin.readline().strip()

            if not hartal:
                break

            hartal = int(hartal)

            for dia in range(hartal-1, int(numDias), hartal):
                if (dia % 7) != 5 and (dia % 7) != 6 :
                    solSet.add(dia)

        solucion += str(len(solSet)) + "\n"

    sys.stdout.write( solucion )