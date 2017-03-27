import sys


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
        
        numWords = int(sys.stdin.readline().strip())

        list_words = []

        for word in range(numWords):
            list_words.append(list(sys.stdin.readline().strip().lower()))

        for word in list_words:

            palEncont = False
            for fila in range(lineas):
                for colum in range(columnas):
                    if list_lines[fila][colum] == word[0]:
                        
                        tamPalab = len(word)
                        
                        #Centro -> Derecha
                        cont = 0
                        punt = 0
                        while( cont < tamPalab ):
                            if colum+punt < columnas and list_lines[fila][colum+punt] == word[cont]:
                                cont += 1
                                punt += 1
                            else:
                                break
                        
                        if( cont == tamPalab ):
                            print( "" + str(fila+1) + " " + str(colum+1) )
                            palEncont = True
                            break
                            
                        #Centro -> Abajo-Derecha
                        cont = 0
                        punt = 0
                        while( cont < tamPalab ):
                            if colum+punt < columnas and fila+punt < lineas and list_lines[fila+punt][colum+punt] == word[cont]:
                                cont += 1
                                punt += 1
                            else:
                                break
                        
                        if( cont == tamPalab ):
                            print( "" + str(fila+1) + " " + str(colum+1) )
                            palEncont = True
                            break
                            
                        #Centro -> Abajo
                        cont = 0
                        punt = 0
                        while( cont < tamPalab ):
                            if fila+punt < lineas and list_lines[fila+punt][colum] == word[cont]:
                                cont += 1
                                punt += 1
                            else:
                                break
                        
                        if( cont == tamPalab ):
                            print( "" + str(fila+1) + " " + str(colum+1) )
                            palEncont = True
                            break
                            
                        #Centro -> Abajo-Izquierda
                        cont = 0
                        punt = 0
                        while( cont < tamPalab ):
                            if colum-punt >= 0 and fila+punt < lineas and list_lines[fila+punt][colum-punt] == word[cont]:
                                cont += 1
                                punt += 1
                            else:
                                break
                        
                        if( cont == tamPalab ):
                            print( "" + str(fila+1) + " " + str(colum+1) )
                            palEncont = True
                            break
                        
                        #Centro -> Izquierda
                        cont = 0
                        punt = 0
                        while( cont < tamPalab ):
                            if colum-punt >= 0 and list_lines[fila][colum-punt] == word[cont]:
                                cont += 1
                                punt += 1
                            else:
                                break
                        
                        if( cont == tamPalab ):
                            print( "" + str(fila+1) + " " + str(colum+1) )
                            palEncont = True
                            break
                            
                        #Centro -> Arriba-Izquierda
                        cont = 0
                        punt = 0
                        while( cont < tamPalab ):
                            if colum-punt >= 0 and fila-punt >= 0 and list_lines[fila-punt][colum-punt] == word[cont]:
                                cont += 1
                                punt += 1
                            else:
                                break
                        
                        if( cont == tamPalab ):
                            print( "" + str(fila+1) + " " + str(colum+1) )
                            palEncont = True
                            break
                            
                        #Centro -> Arriba
                        cont = 0
                        punt = 0
                        while( cont < tamPalab ):
                            if fila-punt >= 0 and list_lines[fila-punt][colum] == word[cont]:
                                cont += 1
                                punt += 1
                            else:
                                break
                        
                        if( cont == tamPalab ):
                            print( "" + str(fila+1) + " " + str(colum+1) )
                            palEncont = True
                            break

                        #Centro -> Arriba-Derecha
                        cont = 0
                        punt = 0
                        while( cont < tamPalab ):
                            if colum+punt < columnas and fila-punt >= 0 and list_lines[fila-punt][colum+punt] == word[cont]:
                                cont += 1
                                punt += 1
                            else:
                                break
                        
                        if( cont == tamPalab ):
                            print( "" + str(fila+1) + " " + str(colum+1) )
                            palEncont = True
                            break
                            
                            
                    if palEncont:
                        break
                
                if palEncont:
                    break;

        if i < int(cases)-1:
            print()
