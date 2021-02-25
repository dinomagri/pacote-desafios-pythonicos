"""
12. linear_merge

Dada duas listas ordenadas em ordem crescente, crie e retorne uma lista
com a combinação das duas listas, também em ordem crescente. Você pode
modificar as listas recebidas.

A sua solução deve rodar em tempo linear, ou seja, deve fazer uma
única passagem em cada uma das listas.
"""


# Essa solução não é linear, pois é necessário passar mais de uma vez para ordenar o resultado final.
def linear_merge(list1, list2):
    return sorted(list1 + list2)

# Usando o pop(-1) com insert também não é linear, pois o insert precisa computar novamente os indices.
def linear_merge(list1, list2):
    res_final = []
    while len(list1) + len(list2) > 0:
        if list1[-1:] > list2[-1:]:
            res_final.insert(0, list1.pop(-1))
        else:
            res_final.insert(0, list2.pop(-1))
    return res_final


# Usando o Heap a regra é respeitada.
from heapq import merge
def linear_merge(list1, list2):
    return list(merge(list1, list2))


# Usando o pop(-1) com append e realizando a inversão da lista já ordenada, a regra é respeitada.
def linear_merge(list1, list2):
    res_final = []
    while len(list1) + len(list2) > 0:
        if list1[-1:] > list2[-1:]:
            res_final.append(list1.pop(-1))
        else:
            res_final.append(list2.pop(-1))
    res_final.reverse()
    return res_final



# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(linear_merge, (['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])
