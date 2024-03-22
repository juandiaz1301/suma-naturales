# Programa para sumar la cantidad de numeros naturales dados por la persona 

#input

n= int(input("Digite el valor de n: "))

# processing

suma = 0
i = 1

while (i <= n):
    suma = suma+i
    i = i + 1

#output
    
print("La suma es ", suma ,)