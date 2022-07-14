# 1.На языке Python или С/С++, написать алгоритм (функцию) определения четности
# целого числа, который будет аналогичен нижеприведенному по функциональности,
# но отличен по своей сути.
# Объяснить плюсы и минусы обеих реализаций.
# Python example:
# def isEven(value):return value%2==0
# C/C++ example:
# bool isEven(int value){return value%2==0;}

import time


# Стандартная функция
# + Быстрая, понятная и легкочитаемая
# - Обязательно должен быть int на входе
def isEven(value: int) -> bool:
    '''
    Функция из задания для определения чётности числа.
    Считаем, что на вход действительно int
    '''
    return value % 2 == 0


# Нестандартная функция
# - Небыстрая, как показали тесты, много времени будет тратиться на корвертацию
# int в str
# + Если же подавать сразу str, то процесс убыстрится.
def is_even(value: str) -> bool:
    '''
    Альтернативная функция для определения чётности.
    Идея в том, что для чётного элемента младший bit = 0,
    то есть число должно оканчиваться на чётные цифры или 0
    '''
    if isinstance(value, str):
        return value[~0] in ('02468')

    str_value = str(value)
    return str_value[~0] in ('02468')


def test_time():
    value_even = 2**1000000
    value_none = 2**1000000 - 1
    value_zero = 0
    start1 = time.time()
    assert isEven(value_even)
    assert not isEven(value_none)
    assert isEven(value_zero)
    stop1 = time.time()
    start2 = time.time()
    assert is_even(value_even)
    assert not is_even(value_none)
    assert is_even(value_zero)
    stop2 = time.time()
    value_even = str(value_even)
    value_none = str(value_none)
    value_zero = str(value_zero)
    start3 = time.time()
    assert is_even(value_even)
    assert not is_even(value_none)
    assert is_even(value_zero)
    stop3 = time.time()
    print('Время работы isEven: ', stop1 - start1, ' сек')
    print('Время работы is_even: ', stop2 - start2, ' сек')
    print('Время работы is_even: ', stop3 - start3, ' сек')
# Время работы isEven:  0.0009999275207519531  сек
# Время работы is_even:  6.2410032749176025  сек
# Время работы is_even:  0.0  сек


if __name__ == '__main__':
    test_time()
