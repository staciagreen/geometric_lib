def area(a, b):
    '''Принимает числа a и b(стороны прямоуг.), возвращает произведение a и b (площадь прямоуг)'''
    if a <= 0 or b <= 0:
        raise ArithmeticError
    return a * b

def perimeter(a, b):
    '''Принимает числа a и b(стороны прямоуг.), возвращает произведение 2 и суммы a и b (периметр прямоуг)'''
    if a <= 0 or b <= 0:
        raise ArithmeticError
    return (a + b) * 2