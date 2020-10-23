# Модуль для построения сводных таблиц из командной строки при помощи функции merging_custom.
# Если его имя merge_new.py, то формат вызова:
# $python merge_new.py -p paths_to_jsons -a paths_to_csvs -o path_to_outfile
# необязательные параметры: -k additional_keys -c columns_to_include
# где
# paths_to_jsons - пути к json-файлам с твитами через пробел без кавычек
# paths_to_csvs - пути к csv-файлам с котировками через пробел без кавычек
# path_to_outfile - путь к выходному csv-файлу без кавычек
# additional_keys - дополнительные ключи json-файла, (кроме даты и текста твита) для включения
# columns_to_include - колонки из csv-файла, которые нужно включить в выходной файл.
# полные наименования параметров:
# -p --people, -a --assets, -o --out, -k --keys -c --columns
# Их тоже можно использовать при вызове модуля вместо сокращенных.
#
# При изменении функции merging_custom ее необходимо заменить и здесь на правильную.

import sys
import argparse
import json
import pandas as pd
import datetime
from merging_custom_function import merging_custom

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--people', nargs='+')
    parser.add_argument('-a', '--assets', nargs='+')
    parser.add_argument('-k', '--keys', nargs='*')
    parser.add_argument('-c', '--columns', nargs='*')
    parser.add_argument('-o', '--out', nargs='+')
    return parser


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    jsons = namespace.people
    csvs = namespace.assets
    outpath = namespace.out[0]
    add_keys = namespace.keys
    add_cols = namespace.columns

    merging_custom(jsons, csvs, outpath, add_keys, add_cols)