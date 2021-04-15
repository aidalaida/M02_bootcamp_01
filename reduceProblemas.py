from functools import reduce

lista = [1,3,-1,15,9]

sumatorio = reduce(lambda x, y: x + y, lista)
#creo una copia de la lista
l = lista[:] 
#añado el neutro para la suma en posición cero, para recorrer la lista desde el ppio
l.insert(0,0)
sumatorioDobles = reduce(lambda x, y: x + y*2, l)

print(sumatorio)
print(sumatorioDobles)