"""

"""

from datetime import datetime
from typing import Sequence

def _parse_krm_line(line: str) -> Sequence:
    """Разобрать строку данных и преобразовать первый элемент
    в «datetime» и следующие во «float». Вернуть список данных.
    """
    result = [datetime.fromisoformat(line[0])] + list(map(float, line[1:]))
    return result

def _split_data(raw_data: str) -> Sequence:    
    """Преобразовать набор данных формата «str» в список с набором
    данных из первого элемента с заголовками столбцов и следующих
    элементов состоящих из данных «datetime» и «float».
    """
    lines = [line.split(',') for line in raw_data.split('\n')]
    header = [line.split()[0] for line in lines[0]]
    data = [_parse_krm_line(line) for line in lines[1:] if len(line) > 2]
    return [header] + data

def _transpose_data(data: list) -> Sequence:
    """Транспонировать список."""
    return list(map(list, zip(*data)))

def parse_data(raw_data: str, transpose: bool=False) -> Sequence:
    """
    Преобразовывает набор данных из строки в список.
    Транспонирует выходные данные при необходимости.

    Параметры:
        raw_data: str - Исходные данные в вимде строки.
        transpose: bool - Флаг запроса на транспонирование данных.
            По умолчанию значение False.

    Возвращаемое значение:
        processed_data (Seauence): Список погодных данных.
    """
    processed_data = _split_data(raw_data)
    if transpose:
        processed_data = _transpose_data(processed_data)
    return processed_data

if __name__ == '__main__':
    from pathlib import Path
    
    from read_data import read_data
    from config import PATH_TO_WEATHER, KRM_LAST_DATE
    
    path = Path(PATH_TO_WEATHER)
    data = read_data(path, KRM_LAST_DATE)
    print(parse_data(data, True)[1][0:10])