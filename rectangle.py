def area(a, b):
    '''Принимает числа a и b(стороны прямоуг.), возвращает произведение a и b (площадь прямоуг)'''
    if a * b <= 0:
        return "inappropriate input parameters"
    return a * b

def perimeter(a, b):
    '''Принимает числа a и b(стороны прямоуг.), возвращает произведение 2 и суммы a и b (периметр прямоуг)'''
    if a * b <= 0:
        return "inappropriate input parameters"
    return (a + b) * 2