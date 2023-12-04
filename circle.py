import math


def area(r):
    '''Возвращает площадь круга с заданным радиусом;
            Параметры:
                    r (float/int) - радиус круга
            Возвращаемое значение:
                    area(float) - площадь круга'''
    if r <= 0:
        raise ArithmeticError
    return math.pi * r * r


def perimeter(r):
    '''Возвращает длину окружности с заданным радиусом;
        Параметры:
                r (float/int) - радиус окружности
        Возвращаемое значение:
                area(float) - периметр окружности'''
    if r <= 0:
        raise ArithmeticError
    return 2 * math.pi * r
