"""
Conjuntos - Set
- É identificado por { }
- Não possui elementos repetidos
- Hash
- Números, String, Tupla -> imutáveis
- Estrutura boa para fazer backtrack *

Análise dos métodos
Complexidade - Operações
Constant => add, remove, in
Linear => for(no order), union, -, intersection

Remover elementos dubplicados em uma lista
"""


def dedup(lst):
    """

    :param lst: list
    :return: uma lista sem números duplicados
    """
    result = []
    repeated = set()
    for e in lst:
        if e not in repeated:
            result.append(e)
            repeated.add(e)
    return result


print(dedup(['banana', 'banana', 'abaxai', 'caqui']))
