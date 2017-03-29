import sys



if __name__ == '__main__':

    while True:
        
        linea = sys.stdin.readline().strip().split()        
        if not linea:
            break
            
        listaNum = list(map(int, linea))
        listaOrg = listaNum[:]
        
        rotaciones = []
        
        orden = sorted(listaNum)
        posicionados = 0
        while( listaNum != orden ):
            posMax = listaNum.index( max( listaNum[:len(listaNum)-posicionados] ) )
            if posMax == 0:
                rotaciones.append(1+posicionados)
                aux = listaNum[:len(listaNum)-posicionados]
                aux.reverse()
                listaNum = aux+listaNum[len(listaNum)-posicionados:]
                posicionados+=1
            else:
                aux = listaNum[:posMax+1]
                aux.reverse()
                listaNum = aux+listaNum[posMax+1:]
                rotaciones.append(len(listaNum)-posMax)


        rotaciones.append(0)
        print(" ".join([str(x) for x in listaOrg]))
        print(" ".join([str(x) for x in rotaciones]))
