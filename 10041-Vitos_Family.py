import sys


if __name__ == '__main__':
    casos = int(sys.stdin.readline())
    for caso in range(casos):
        
        linea = sys.stdin.readline().strip().split(" ")
        nCasas = int(linea[0])
        casas = linea[1:]
        map(int, casas)
        
        #print("nCasas: " + str(nCasas))
        #print(casas)
        
        sorted(casas)
        pos = int(nCasas/2)
            
        #print(pos)
        #print(casas[pos-1])
        
        casaVito = int(casas[pos])
        
        suma = 0
        for casa in casas:
            suma += abs(int(casa) - casaVito)
        
        print(suma)