#En todos los casos:
#
# start es inclusive (se toma en cuenta)
#
# stop es exclusive (no se toma en cuenta, es decir, que el recorrido termina lo máximo
# posible que se puede quedar cerca de este sin llegar a el)

n = 5

#for(int  i = 0; i<n; i++){sout(i);}

print("Recorrido de 0 a n (por defecto con incrmentos de 1 en 1)")
for i in range(n):
    print(i)

print()

print("Recorrido de 2 a n (por defecto con incrementos de 1 en 1)")
for i in range(2, n):
    print(i)


print()

print("Recorrido Normal, pero con incrementos de 3 en 3 ")
n = n*n
for i in range(2, n,3):
    print(i)

print()
print("Recorrido Inverso:")
for i in range(n,2,-2):
    print(i)


print("Recorrido Inverso Ejemplo 2:")
for i in range(0,-20,-2):
    print(i)

