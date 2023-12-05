import argparse
from datetime import datetime
import os
from dataclasses import dataclass
import json

INTRO_PATH = '/mnt/weather/weather/krm_min/'
OUTRO_PATH = '/media/larm_data/samba/data/meteo_data'

@dataclass(slots=True, frozen=True)
class Weather:
    dates: list[datetime]
    

def get_lastdate(path: str) -> datetime:
    # Получить дату последних имеющихся данных.
    with open(os.path.join(INTRO_PATH, 'lastdate.txt'), 'r') as lastdate_file:
        lastdate = lastdate_file.readline()
        date = datetime.fromisoformat(lastdate)
    return date

def generate_path_to_intro_file(date: datetime, path: str) -> str:
    # Сформировать путь к файлу с данными.
    return os.path.join(path, str(date.year), str(date.month), f"{date:%Y-%m-%d}.txt")

def generate_path_to_outro_file(date: datetime, path: str) -> str:
    # Сформировать путь к файлу с данными.
    return os.path.join(path, str(date.year), str(date.month), f"{date:%Y%m%d}_KRM_meteo.txt")

def parse_date(raw_data: list):
    # Преобразовать данные из файла.
    header = [column_name.split()[0] for column_name in raw_data[0]]
    datarows = [[line[0]] + list(map(float, line[1:])) for line in raw_data[1:]]
    transposed_data = list(zip(*datarows))
    data = dict(zip(header, transposed_data))
    return data

def get_data(date: datetime, path: str) -> list:
    # Получить данные из файла и преобразовать.
    filename = generate_path_to_intro_file(date, path)
    with open(filename, 'r') as file:
        raw_data = [line.strip().split(', ') for line in file.readlines()]
        data = parse_date(raw_data)
    return data

def write_data_to_txt(path: str, date: datetime) -> None:
    return None

def main():
    date = get_lastdate(INTRO_PATH)
    data = get_data(date, INTRO_PATH)   
    # with open("out.json", 'w') as outfile:
    #     json.dump(data, outfile)

if __name__ == "__main__":
    main()