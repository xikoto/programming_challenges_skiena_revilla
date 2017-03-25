import sys


if __name__ == '__main__':
    
    casos = int(sys.stdin.readline())
    sys.stdin.readline()
    
    for caso in range(casos):
        
        diccionario = dict()
        
        while True:
            
            fragmento = sys.stdin.readline().strip()
            
            if not fragmento:
                break
            else:
                
                tamFrag = len(fragmento)
                
                if tamFrag in diccionario:
                    diccionario[tamFrag].append(fragmento)
                else:
                    diccionario[tamFrag] = [fragmento]
                
        
        tamanyos = sorted(diccionario.keys())
        combinaciones = []
        
        i = 0
        j = len(tamanyos)-1
        
        while i<=j:
            conjunto = set()
            
            izq = diccionario[tamanyos[i]]
            der = diccionario[tamanyos[j]]
            
            for fragIzq in izq:
                for fragDer in der:
                    conjunto.add(fragIzq+fragDer)
                    conjunto.add(fragDer+fragIzq)
                    
            combinaciones.append(conjunto)
            i += 1
            j -= 1
            
        
        soluciones = combinaciones[0]
        
        for i in range(len(combinaciones)-1):
            soluciones = soluciones.intersection( combinaciones[i+1] )
            
        print( list(soluciones)[0] )
        
        if caso < casos-1:
            print()
        
        