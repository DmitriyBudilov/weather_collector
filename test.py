import argparse

parse = argparse.ArgumentParser(description="Сбор погодных данных с сервера //df1.emsd.ru/public/weather/")
parse.add_argument('-d', '--date', type=str, default=None, help="Дата дня ")
parse.add_argument('-ds', '--dates', type=list, nargs='*', help="")
parse.add_argument('-st', '--station', type=str, help="")

print('test\n')
namespace = parse.parse_args()
print(namespace)