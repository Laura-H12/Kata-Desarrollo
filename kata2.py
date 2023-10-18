def cuadrados(matriz):
    
    matriz.sort()
      
    cuadrados_menores=[]
    for num in matriz:
       cuadrado = num ** 2
       if cuadrado < 99:
           cuadrados_menores.append(cuadrado)
    
    cuadrados_menores.sort()
       
    print("Matriz:", matriz)
    print("Matriz de cuadrados menores a 99:", cuadrados_menores)


numeros = [-1, -2, 3, 4, -5,10]
cuadrados(numeros)
