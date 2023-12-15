from typing import Protocol
from pathlib import Path
from datetime import datetime

from exceptions import NoDataFile

class Weather(Protocol):
    """Интерфейс для погодных данных.
    """    
    def read_data(self) -> None:
        raise NotImplementedError

    def parse_data(self) -> None:
        raise NotImplementedError

    def wreate_data(self) -> None:
        raise NotImplementedError

class WeetherKoz:
    
    def __init__(self, base_path: str, date: datetime=None) -> None:
        self.path = base_path
        self.date = date


    def read_data(self) -> None:
        pass

    def parse_data(self) -> None:
        pass

    def wreate_data(self) -> None:
        pass

    def _generate_path(base_directory: Path, searched_date: date) -> Path:
        """Сгенерировать путь к текстовому файлу из пути к котологу с данными и даты."""
        path = base_directory.joinpath(*map(str, (searched_date.year,
                                                searched_date.month,
                                                searched_date))).with_suffix('.txt')
        return path

    def _get_last_date(base_directory: Path, filename: str) -> date:
        """Получить дату последних доступных данных."""
        path = Path(base_directory, filename)
        with open(path, 'r') as file:
            lastdate = file.read().split()[0]
        return date.fromisoformat(lastdate)

    def _read_data(path: Path) -> str:
        """Получить данные из файла и вернуть в виде строки."""
        if not path.exists():
            raise NoDataFile
        with open(path, 'r') as file:
            data = file.read()
        return data

    def read_data(base_directory: Path, lastdate_file: str, searched_date: date=None) -> str:
        """Получить данные за указанную дату."""
        if not searched_date:
            searched_date = _get_last_date(base_directory, lastdate_file)
        path = _generate_path(base_directory, searched_date)
        return _read_data(path)




def main():
    pass


if __name__ == "__main__":
    main()