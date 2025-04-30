'''Задача: пройтись кругом по элементам от 1 до n
и напечатать первое число каждого интервала m
в этом круге. Ходить следует до тех пор, пока конечным
элементом не станет единица.
В качестве ответа вывести все первые числа.'''
import sys
from itertools import cycle


def task_1(n: int, m: int) -> list[int]:
    '''Делаем из числа n диапазон и
    проходим по нему бесконечным циклом.
    Добавляем числа в mini и обнуляем mini
    каждый раз, когда он достигает размера n.
    Если mini закончится на 1, то разрушаем цикл
    и возвращаем result.'''
    result = []
    mini = []  # здесь будут сохраняться m чисел.
    for number in cycle(range(1, n + 1)):
        mini.append(number)
        if len(mini) == m:
            result.append(mini[0])
            if mini[-1] == 1:
                break
            mini = [number]
    return result


if __name__ == "__main__":
    n, m = map(int, sys.argv[1:])
    print(*task_1(n, m), sep='')

    