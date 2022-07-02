
#assert
if __name__ == '__main__':
    try:
        assert 'hola' == 'Hola', 'Sorry, its not the same, hola with Hola'
        """
        if not 'hola' == 'Hola':
            raise AssertionError("Sorry, its not the same, hola with Hola")
        """
        print('>>> El programa continua con su ejecuci[on.')
    except AssertionError as error:
        print(error)

print('')
print('==================================================================')
print('')

def suma_numeros_positivos(n1: int, n2: int) -> int:
    """Sumar dos numeros enteros positivos.

    Args:
        n1 (int): _description_
        n2 (int): _description_

    Returns:
        int: _description_
    """

    assert n1 > 0 and n2 > 0, 'Sorry, this only works with positive numbers'
    return n1 + n2

if __name__ == '__main__':
    resul = suma_numeros_positivos(100,200)
    print(resul)