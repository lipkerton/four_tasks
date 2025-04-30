'''Задача: распарсить tests.json
для каждого значения value в tests.json
присвоить соответствующее значение в values.json.'''
import json
import pathlib
import sys


def assign_value(
    tests: dict[str, int, list],
    values: list[dict]
) -> None:
    '''Ищем нужный id в values и поставляем
    value из values в value из tests.'''
    for value in values:
        value_id = value.get('id')
        tests_id = tests.get('id')
        if value_id == tests_id:
            tests['value'] = value['value']


def parse_tests(
    tests: dict[str, int, list],
    values: list[dict],
) -> list[dict] | dict[str, int, list]:
    '''Рекурсия - получаем словарь, смотрим в значение
    values: если есть список из словарей внутри, то погружаемся.
    Перед погружением выставляем значение value.
    Перед выходом из рекурсии выставляем значение value.'''
    tests_values = tests.get("values")
    if not tests_values:
        assign_value(tests, values)
        return tests
    assign_value(tests, values)
    for test in tests_values:
        parse_tests(test, values)
    return tests["values"]


def main(
    tests_data: dict[str, int, list],
    values_data: dict[list]
) -> list[dict]:
    '''Проходим по всем словарям в списке tests.
    Каждый словарь отправляем в функцию parse_tests.
    Результаты сохраняем в result.'''
    result = []
    for test in tests_data['tests']:
        result.append(parse_tests(test, values_data["values"]))
    return result

if __name__ == "__main__":
    tests_json, values_json, report_json = sys.argv[1:]

    tests_json = pathlib.Path(tests_json).absolute()
    values_json = pathlib.Path(values_json).absolute()
    report_json = pathlib.Path(report_json).absolute()

    if tests_json.exists() and values_json.exists():
        with open(tests_json, 'r') as file_1:
            tests_data = json.load(file_1)
        with open(values_json, 'r') as file_2:
            values_data = json.load(file_2)

    result = dict()
    result["tests"] = main(tests_data, values_data)

    with open(report_json, 'w') as file_3:
        result = json.dumps(result, indent=2)
        file_3.write(result)