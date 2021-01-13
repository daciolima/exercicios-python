from random import shuffle


def max_min(lst):
    """
    Calcule o valor maxino e minino de uma lista
    :param lst: list
    :return: tuple: (max, min)
    """
    n = len(lst)
    if n == 0:
        raise ValueError('Lista está em branco')
    max_valor = min_valor = lst[-0]

    def max_min_rec(cursor):
        """
        t(n) = 1 + t(n-1)
        t(n) = 1 + 1 + t(n-2)
        t(n) = 1 + 1 + 1 + t(n-3)
        t(n) = 1 + 1 + 1 +  ...t(-1)
        t(n) = n + 1 => 0(n)

        m(m) = 1 + m(n-1) => 0(n)
        OBS: Como o python não tem otimização de calda, a recursividade acaba sendo de complexidade Linear

        :param cursor:
        :return:
        """

        nonlocal max_valor, min_valor
        if cursor < 0:
            return max_valor, min_valor
        current = lst[cursor]
        if current > max_valor:
            max_valor = current
        if current < min_valor:
            min_valor = current
        return max_min_rec(cursor - 1)
    return max_min_rec(n - 1)


print(max_min([1]))
print(max_min([1, 2]))
lista_random = list(range(100))
shuffle(lista_random)
print(lista_random)
print(max_min(lista_random))
print(max_min([]))

