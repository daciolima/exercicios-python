""" Listas

Análise
#########################################
Complexidade => Operações
Contant => [i], [i] = x, append, pop, len
Linear => in, index, for, count, [begin: end], extend, +, *, reverse, remove, insert, shuffle, split, join
Sublinear => Sort, Sorted
#########################################
"""
# Exemplos - Operações em tempo Contante
# [i], [i] = x,
lista = list(range(1, 11))
print(lista[0],  lista[-1])

# append
lista.append(12)
print(lista)

# pop
resultado = lista.pop()
print(lista, resultado)

# len
print(len(lista))


# Exemplos - Operações em tempo Linear
# in, index, for, count, [begin: end], extend, +, *, reversed, remove, insert, shuffle, split, join
# for
for i in lista:
    print(i)

# index
print(f'O número index do elemento 1 é: {lista.index(1)}')

# count
print(f'Número de vezes que o elemento 5 aparece na lista: {lista.count(5)}')

# [:] =>  Slice
print(f'A fatia de 0 até 5 é: {lista[0:6]}')

# + =>  Concatenação
lista2 = list(range(11, 21))
print(f'A concatenação das listas: lista e lista2 é:\n{lista + lista2}')

# * =>   Multiplica uma lista pela quantidade do elemento passando
print(f'A lista multiplicada por 2 é: {lista * 2}')

# extend =>   Altera uma lista acrescentando ao final o elemento passado como argumento
lista2.extend(lista)
print(f'A lista2 foi alterada passando a conter:\n{lista2}')

# reversed =>  cria uma lista reversa com o elemento passado por argumento
print(list(reversed(lista)))
print(lista)

# reverse =>  Altera uma lista tornando-a reversa
lista.reverse()
print(lista)

# insert
# Inclui um elemento em um determinado index. Obs: Se a inserção ou remoção ocorrer no iniciou
# ou no meio isso é custoso, pois deve-se alterar todos os indeces dos demais elementos.
lista.insert(0, 33)
print(lista)
lista.pop(0)
print(lista)

# shuffle => Embaralha uma lista
from random import shuffle
shuffle(lista)
print(lista)

# split => A partir de uma String pode se obter uma lista fatiando no valor(es) passado(s) no split
frase = 'Dácio é um cara legal.'
print(frase.split())
print(frase.split('c'))

# join => Uni elementos de uma retornando a uma String
fatiado = frase.split()
print(','.join(fatiado))


# Exemplos - Operações em tempo Sublinear
# sorted() e sort()
# sorted => Ordena elementos de uma lista não alterando-a
print(sorted(lista))
print(lista)

# sort => Altera uma lista ordenando os elementos.
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)








