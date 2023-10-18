def cambio(numeros):
    numeros.sort()  
    menor = 1  

    for num in numeros:
        if num <= menor:
            menor += num
        else:
            break

    return menor

monedas = [1,2,4]
result = cambio(monedas)
print("El mínimo cambio que NO puede dar es:" , result)