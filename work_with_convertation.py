import os
import sqlite3
import pandas as pd


def process_conversion(convertation_file):
    if convertation_file == 'txt_to_csv':
        filename = input('Введите название файла: ')
        with open(filename, 'r', encoding='utf-8') as txt_file:
            content = txt_file.read()

        lines = content.split('\n')

        df = pd.DataFrame(lines)
        df.to_csv('file.csv', index=False)

    elif convertation_file == 'csv_to_xlsx':
        namefile = input('Введите название файла: ')

        read_file = pd.read_csv(namefile)
        delimiter = namefile.split('.')[0]
        read_file.to_excel(f'{delimiter}.xlsx', index=None, header=True)

    elif convertation_file == 'xlsx_to_csv':
        namefile = input('Введите название файла: ')

        read_file = pd.read_excel(namefile)
        delimiter = namefile.split('.')[0]
        read_file.to_csv(f'{delimiter}.csv', index=None, header=True)
        os.remove(namefile)

    elif convertation_file == 'csv_to_sql':
        input_name_file_csv = input('Введите название файла: ')

        input_name_file_sql = input('Введите название файла: ')

        conn = sqlite3.connect(input_name_file_sql)

        df = pd.read_csv(input_name_file_csv)
        df.to_sql('contact', conn, if_exists='append', index=False)

    elif convertation_file == 'sql_to_csv':
        print('???')