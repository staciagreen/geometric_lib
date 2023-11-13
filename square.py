
def area(a):
    '''Принимает число a (сторону квадр.), возвращает квадрат a (площадь квадр.)'''
    if a <= 0:
        raise ArithmeticError
    return a * a


def perimeter(a):
    '''Принимает число a (сторону квадр.), возвращает произведение 4 и a (периметр квадр.)'''
    if a <= 0:
        raise ArithmeticError
    return 4 * a
