import sys

if __name__ == '__main__':
    casos = int(sys.stdin.readline())
    for caso in range(casos):
        
        linea = sys.stdin.readline().strip().split(" ")
        nCasas = int(linea[0])
        casas = linea[1:]
        casas = sorted(list(map(int, casas)))

        pos = int(nCasas/2)

        
        casaVito = casas[pos]
        
        suma = 0
        for casa in casas:
            suma += abs(casa - casaVito)
        
        print(suma)
