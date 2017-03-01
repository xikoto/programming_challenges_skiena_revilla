import sys
from itertools import groupby
from collections import defaultdict

if __name__ == '__main__':

    cont = 0
    rondas = []
    categorias = defaultdict(list)
    rondAux = []

    while True:
        rondas = []
        for i in range(13):
            ronda = sys.stdin.readline().strip().split()
            if not ronda:
                break
            rondas.append(ronda)
        if not ronda:
            break


        for rond in rondas:
            value = (0,0)

            resXaxi = [len(list(group)) for key, group in groupby(rond)]

            if resXaxi.__contains__(3) and resXaxi.__contains__(2): #FullHouse


