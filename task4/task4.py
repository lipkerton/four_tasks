'''Задача: вычислить сколько минимально
ходов потребуется, чтобы привести все элементы
массива к одинаковым значениям. За один ход
можно прибавлять или отнимать только единицу.'''
import sys
import pathlib


def main(input_data: list[int]) -> int:
    '''Вычисляем медиану (минимальное нужное значение),
    а потом проходимся функцией map по сортированному массиву,
    вычитаем из каждого элемента медиану, получаем абсолютное
    значение. Результаты суммируем.'''
    median = input_data[len(input_data) // 2]
    return sum(map(lambda number: abs(number - median), input_data))


if __name__ == "__main__":
    input_file = sys.argv[1:][0]
    input_file = pathlib.Path(input_file).absolute()
    if input_file.exists():
        with open(input_file, 'r') as file:
            input_data = sorted(map(int, file.readlines()))
        print(main(input_data))