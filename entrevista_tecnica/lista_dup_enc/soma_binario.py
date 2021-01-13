"""
Lista Duplamente Encadeada:
- É dinâmica… Pode ser inserido elementos de forma arbitrária
- Funciona bem como Pilha e Fila
- Funciona muito bem para iteração como a lista
- Não funciona bem para acessar elementos no meio da estrutura(aleatórios)
- Pertence ao pacote collections.deque *

Análise:
Complexidade e Operações:
Constant: append, appendleft, pop, popleft, len
Linear: [ i ], [ i ] = x, extend, extendleft
"""


def soma_binario(n, n2):
    """
    Soma de números binários não negativos
    :param n: String
    :param n2: String
    :return: binary
    """

    n = int(n, 2)  # Argumento e base 2
    n2 = int(n2, 2)  # Argumento e base 2
    return format(n + n2, 'b')  # format() Método com segundo um parametro para retorno desejado. 'b' => binary


print(soma_binario("111110", "1100"))  # 1001010
