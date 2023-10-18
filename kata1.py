from random import randint

n=100
numeros=[]

for i in range(n):
    numero=randint(0,99)
    numeros.append(numero)

S=9
R= 99
numeros_sin_9 = []

for num in numeros:
    if num ==S or num==R:
        numeros.remove(num)
    else:
        num_escrito = str(num)
        nuevo_numero = ""

    for digito in num_escrito:
        if int(digito) != S:
            nuevo_numero += digito

    numeros_sin_9.append(int(nuevo_numero))

numeros_sin_9.reverse()
print(numeros)
print(numeros_sin_9)