from openpyxl import load_workbook
import pandas as pd
import sys
import os


def process_csv(filename):
    command = int(input('Введите режим:'
                     '\n1) - чтение\n'
                     '2) - добавление\n'
                     '3) - удаление\n'
                     '4) - разделить файл\n'
                     '5) - переименовать\n'))

    if command == 1:
        name_file = input('Введите название файла: ')
        pd.read_csv(name_file, delimiter=',')

    elif command == 3:
        mode2 = int(input('Вы хотите удалить столбец или строчку (1,2): '))
        if mode2 == 1:
            mode3 = int(input('Вы хотите удалить один столбец или сразу несколько (1,2): '))
            if mode3 == 1:
                col = input('Введите столбец который хотите удалить: ')

                df = pd.read_csv(filename, on_bad_lines='skip', sep=";", index_col=0)
                df_marks = df.drop(columns=col)
                print(df_marks)

                df1 = pd.DataFrame(df_marks)
                df1.to_csv(filename)

            elif mode3 == 2:
                pd.set_option("display.max.columns", 100)

                df = pd.read_csv(filename, on_bad_lines='skip', sep=";", index_col=0)
                print(df.columns)
                print(df.head(5))

                cols = input('Введите столбцы, которые хотите удалить (через пробел): ').split()

                for col in cols:
                    if col in df.columns:
                        df = df.drop(columns=col)

                df.to_csv(filename, sep=";")
                print(df)
    elif command == 4:
        mode = int(input('Введите режим (1 - ручной / 2 - автоматический): '))
        if mode == 1:
            # Ручной поиск

            pd.set_option("display.max.columns", 100)
            pd.set_option("display.max.rows", 100)

            df = pd.read_csv(filename, on_bad_lines='skip')

            m = int(input('Введите с какой строки вы хотите ввести: '))

            n = int(input('Введите по какую строку вы хотите ввести: '))

            new_filename = input('Введите новое название файла: ')

            delenyie = df.iloc[m:n]

            df2 = pd.DataFrame(delenyie)
            df2.to_csv(new_filename)

            print('Все успешно сохранилось')

        elif mode == 2:
            #Автоматический поиск

            pd.set_option("display.max.columns", 100)
            pd.set_option("display.max.rows", 100)

            df = pd.read_csv(filename, on_bad_lines='skip')
            print(len(df))

            chunk_size = 1000000

            num_chunk_size = len(df) // chunk_size + 1
            print(num_chunk_size)

            for i in range(num_chunk_size):
                start_index = i * chunk_size
                end_index = (i + 1) * chunk_size
                chunk = df[start_index:end_index]
                chunk.to_csv(f'party_zdravcity_{i}.csv', index=False)
            print('Все успешно сохранилось')

    elif command == 5:
        column = input('Введите колонку которую вы хотите перименовать: ')
        new_column = input('Введите новую колонку: ')

        df = pd.read_csv(filename, on_bad_lines='skip', sep=";", index_col=0)
        df_rename = df.rename(columns={column: new_column})
        df2 = pd.DataFrame(df_rename)
        df2.to_csv(filename)

    elif command == 'quit':
        print('Вы успешно вышли из программы')

    else:
        print('Ошибка')


def process_xlsx(filename):
    mode = int(input('Введите режим:'
                     '\n1) - чтение\n'
                     '2) - запись\n'
                     '3) - удаление\n'
                     '4) - разделить файл\n'
                     '5) - переименовать файл\n'))

    if mode == 1:
        df_orders = pd.read_excel(filename, index_col=0)
        print(df_orders.head())

    elif mode == 2:
        a = int(input('Введите индекс: '))
        b = int(input('Введите колонку: '))

    elif mode == 3:
        col = input('Введите столбец который хотите удалить: ')
        df = pd.read_excel(filename, index_col=0)
        df_marks = df.drop(columns=col)
        print(df_marks)

    elif mode == 4:
        n = int(input('Введите до скольки нужно разделить файл: '))

        df = pd.read_excel(filename)
        read = df.head(n)
        print(read)

        df1 = pd.DataFrame(read)
        df1.to_csv('new_file.xlsx')

        df.drop(labels=[read], axis=0)

    elif mode == 5:
        column = input('Введите колонку которую вы хотите перименовать: ')
        new_column = input('Введите новую колонку: ')

        df = pd.read_excel(filename, index_col=0)
        df_rename = df.rename(columns={column: new_column})
        df2 = pd.DataFrame(df_rename)
        df2.to_excel(filename)


def process_txt(filename):
    mode = int(input('Введите режим:'
                     '\n1) - чтение\n'
                     '2) - запись\n'
                     '3) - добавление\n'
                     '4) - удаление\n'
                     '5) - разделить файл\n'))

    if mode == 1:
        with open(filename, 'r') as f:
            print(f.read())

    elif mode == 2:
        with open(filename, 'w') as f:
            content = input('Введите что вы хотите записать: ')
            f.write(content)

    elif mode == 3:
        with open(filename, 'a') as f:
            content = input('Введите что вы хотите добавить: ')
            f.write(content)

    elif mode == 4:
        with open(filename, 'w') as f:
            f.write('')
            f.close()

    elif mode == 5:
        while True:
            file = open(f"{filename}", "r")

            chunk_size = 1000000

            num_chunk_size = len(open(f'{filename}').readlines()) // chunk_size + 1
            print(num_chunk_size)

            m = int(input('Введи со скольки ты хочешь разделить: '))

            n = int(input('Введи до скольки ты хочешь разделить: '))

            new_filename = input('Придумайте новое название для файла: ')

            lines = file.readlines()[m:n]

            for line in lines:
                print(line.replace('\n', ''))

                with open(f'{new_filename}', 'w') as f:
                    f.writelines(lines)


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


def converter():
    print('программа converter предназначена для работы с файлами и всякими расширениями')

    extension = input('Введите с каким расширением вы хотите работать (csv, xlsx, txt, con): ')

    if extension == 'csv':
        filename = input('Введите название файла: ')
        process_csv(filename)

    elif extension == 'xlsx':
        filename = input('Введите файл: ')
        process_xlsx(filename)

    elif extension == 'txt':
        filename = input('Введите название файла: ')
        process_txt(filename)

    elif extension == 'con':
        convertation_file = input('Введите из какого файла в какой вы хотите переконвертировать: ')
        process_conversion(convertation_file)

    elif extension == 'quit':
        sys.exit()


def main():
    converter()


if __name__ == '__main__':
    main()