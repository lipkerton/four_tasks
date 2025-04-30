'''Задача: определить принадлежат ли точки
к окружности.'''
import pathlib
import sys


def main(
    x_center: float,
    y_center: float,
    radius: float,
    coords: list[float]
) -> list[int]:
    '''Берем координаты радиуса,
    величину радиуса, координаты точек.
    Вычисляем квадрат расстояния до центра
    окружности по формуле.
    Сравниваем квадрат расстояния
    с квадратом радиуса.'''
    result = []
    for i in range(0, len(coords) - 1, 2):
        x = coords[i]
        y = coords[i + 1]
        dx = x - x_center
        dy = y - y_center
        distance_sq = dx**2 + dy**2
        radius_sq = radius**2
        if distance_sq < radius_sq:
            result.append(1)
        elif distance_sq == radius_sq:
            result.append(0)
        else:
            result.append(2)
    return result


if __name__ == "__main__":
    cord_rad, cord_point = sys.argv[1:]
    cord_rad = pathlib.Path(cord_rad).absolute()
    cord_point = pathlib.Path(cord_point).absolute()
    if cord_rad.exists() and cord_point.exists():
        with open(cord_rad, 'r') as file_1:
            x_center, y_center = map(
                float, file_1.readline().split()
            )
            radius = float(file_1.readline())
        with open(cord_point, 'r') as file_2:
            coords = list(map(
                float, file_2.read().split()
            ))
        print(
            *main(x_center, y_center, radius, coords), sep='\n'
        )