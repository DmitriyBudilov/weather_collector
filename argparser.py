import argparse
from argparse import Namespace
from datetime import datetime, date

def get_args() -> Namespace:
    "Вернуть аргументы вызова утилиты."

    parser = argparse.ArgumentParser(
        prog="Погода",
        description="Утилита сбора погодных данных.",
        epilog="Футер"
        )

    parser.add_argument(
        'location',
        type=str,
        metavar='',
        # dest='location',
        choices=('krm', 'koz', 'kly', 'skr', 'prt', 'pet'),
        help='Код станции.'
    )

    parser.add_argument(
        '-d',
        '--date',
        type=str,
        metavar='',
        default=None,
        dest='date',
        help='Дата в формате iso «YYYY-MM-DD».'
    )

    parser.add_argument(
        '-ds',
        '--dates',
        type=list,
        metavar='',
        dest='dates',
        nargs='+',
        help='Вызов утилиты для нескольких дат.'
    )

    parser.add_argument(
        '-ld',
        '--lastdate',
        action='store_true',
        dest='last_date',
        help='Последняя доступная дата.'
    )

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    print(get_args())
    date.utcnow().isoformat()