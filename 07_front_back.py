"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""
import math


def front_back_manual(a, b):
    size_a = len(a)
    size_b = len(b)
    if size_a % 2 == 0 and size_b % 2 == 0:
        size_a, size_b = size_a // 2, size_b // 2
        front_a = a[:size_a]
        back_a = a[size_a:]
        front_b = b[:size_b]
        back_b = b[size_b:]
        return front_a + front_b + back_a + back_b

    elif size_a % 2 == 1 and size_b % 2 == 1:
        size_a, size_b = (size_a // 2) + 1, (size_b // 2) + 1
        front_a = a[:size_a]
        back_a = a[size_a:]
        front_b = b[:size_b]
        back_b = b[size_b:]
        return front_a + front_b + back_a + back_b
    elif size_a % 2 == 1 and size_b % 2 == 0:
        size_a, size_b = (size_a // 2) + 1, (size_b // 2)
        front_a = a[:size_a]
        back_a = a[size_a:]
        front_b = b[:size_b]
        back_b = b[size_b:]
        return front_a + front_b + back_a + back_b
    elif size_a % 2 == 0 and size_b % 2 == 1:
        size_a, size_b = (size_a // 2), (size_b // 2) + 1
        front_a = a[:size_a]
        back_a = a[size_a:]
        front_b = b[:size_b]
        back_b = b[size_b:]
        return front_a + front_b + back_a + back_b


def front_back_math(a, b):
    size_a = len(a)
    size_b = len(b)
    front_a = a[:math.ceil(size_a/2)]
    back_a = a[math.ceil(size_a / 2):]
    front_b = b[:math.ceil(size_b / 2)]
    back_b = b[math.ceil(size_b / 2):]
    return ''.join([front_a, front_b, back_a, back_b])


def front_back(a, b):
    idx_a = math.ceil(len(a) / 2)
    idx_b = math.ceil(len(b) / 2)
    return ''.join((a[:idx_a], b[:idx_b], a[idx_a:], b[idx_b:]))


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
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
    test(front_back, ('Donut', 'Kitten'), 'DonKitutten')
