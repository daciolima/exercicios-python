from random import shuffle


def max_min(lst):
    """
    Calcule o valor maxino e minino de uma lista
    :param lst: list
    :return: tuple: (max, min)
    """
    if len(lst) == 0:
        raise ValueError('Lista está em branco')
    max_valor = min_valor = lst[0]

    for valor in lst:
        if valor > max_valor:
            max_valor = valor
        if valor < min_valor:
            min_valor = valor

    return min_valor, max_valor


print(max_min([1]))
print(max_min([1, 2]))
lista_random = list(range(100))
shuffle(lista_random)
print(lista_random)
print(max_min(lista_random))
print(max_min([]))

