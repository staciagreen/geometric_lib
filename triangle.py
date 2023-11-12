def area(a, h):
    '''Принимает числа a и h(сторону треуг. и высоту), возвращает частное произведения a и h и 2 (площадь треуг)'''
    if a * h == 0:
        return "inappropriate input parameters"
    return a * h / 2


def perimeter(a, b, c):
    '''Возвращает периметр треугольника с заданными сторонами;
        Параметры:
                a (float/int) - первое 
        Возвращаемое значение:
                area(float) - площадь круга'''
    if a * b * c == 0:
        return "inappropriate input parameters"
    return a + b + c
