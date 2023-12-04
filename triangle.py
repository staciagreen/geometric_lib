def area(a, h):
    '''Принимает числа a и h(сторону треуг. и высоту), возвращает частное произведения a и h и 2 (площадь треуг)'''
    if a <= 0 or h <= 0:
        raise ArithmeticError
    return a * h / 2


def perimeter(a, b, c):
    '''Возвращает периметр треугольника с заданными сторонами;
        Параметры:
                a (float/int) - первое 
        Возвращаемое значение:
                area(float) - площадь круга'''
    if a * b * c <= 0 or b * c <= 0 or not (a + b > c and b + c > a and a + c > b):
        raise ArithmeticError
    return a + b + c
