miset = {'rojo', 'azul', 'verde'}   #Los elementos no se pueden indexar.    Elimina los elementos duplicados
print(miset)
lista = ['rojo', 'azul', 'verde', 'rojo', 'azul', 'verde']
print(set(lista))
listaUnicos= list(set(lista))
print(listaUnicos)

fset= frozenset({'azul', 'verde', 'amarillo'})
print(fset)