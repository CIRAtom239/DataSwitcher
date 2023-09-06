import pandas as pd
import sqlite3
import random
import time
import sys
import os


def process_csv(filename):
    command = int(input('Введите режим:'
                     '\n1) - чтение\n'
                     '2) - добавление\n'
                     '3) - удаление\n'
                     '4) - разделить файл\n'
                     '5) - переименовать\n'
                     '6) - объединение\n'))

    if command == 1:
        pd.set_option("display.max.columns", 100)
        pd.set_option("display.max.rows", 100)

        df = pd.read_csv(filename, delimiter=',')
        print(df)

    elif command == 2:
        command2 = int(input('Введите вы хотите добавить строку или столбец (1,2): '))

        if command2 == 1:
            df = pd.read_csv(filename)
            for dataframe in df.columns():
                examination = dataframe.dtypes

                print(examination)

                if examination == 'int64':
                    meaning_int = int(input('Введите новое значение в эту колонку: '))
                    df[dataframe] = df[meaning_int]
                    new_dataframe_int = pd.DataFrame()

                elif examination == 'object':
                    meaning_object = input('Введите новое значение в эту колонку: ')

                elif examination == 'float64':
                    meaning_float = input('Введите новое значение в эту колонку: ')

        elif command2 == 2:
            command3 = int(input('Введите вы хотите добавить один столбец или несколько (1,2): '))
            if command3 == 1:
                df = pd.read_csv(filename)
                player_vals = input('Введите название новой колонки: ')
                df.insert(loc=0, column='player', value=player_vals)
            elif command3 == 2:
                kol_new_column = int(input('Введите количество новых колонок: '))
                a = []
                df = pd.read_csv(filename)
                for i in range(1,kol_new_column):
                    player_vals = input('Введите название новой колонки: ')
                    a.append(player_vals)
                df.insert(loc=0, column=a)

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

                cols = input('Введите столбцы, которые хотите удалить: ')

                for col in cols:
                    if col in df.columns:
                        df = df.drop(columns=col)

                df.to_csv(filename, sep=";")
                print(df)

        elif mode2 == 2:
            print('???')

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

            chunk_size = int(input('Введите оптимальный chunk_size: '))

            j = input('Введите название нового файла: ')

            num_chunk_size = len(df) // chunk_size + 1
            print(num_chunk_size)

            for i in range(num_chunk_size):
                start_index = i * chunk_size
                end_index = (i + 1) * chunk_size
                chunk = df[start_index:end_index]
                chunk.to_csv(f'{j}_party_{i}.csv', index=False)
            print('Все успешно сохранилось')

    elif command == 5:
        column = input('Введите колонку которую вы хотите перименовать: ')
        new_column = input('Введите новую колонку: ')

        df = pd.read_csv(filename, on_bad_lines='skip', sep=";", index_col=0)
        df_rename = df.rename(columns={column: new_column})
        df2 = pd.DataFrame(df_rename)
        df2.to_csv(filename)

    elif command == 6:
        command_union = int(input('Вы хотите объеденить только два файла или несколько (1,2): '))
        if command_union == 1:
            df1 = input('Введите первый файл: ')
            df2 = input('Введите второй файл: ')

            a = pd.read_csv(df1)
            b = pd.read_csv(df2)

            print(df1)
            print(df2)

            df3 = pd.concat([a, b])
            df3.to_csv('new_party_file.csv', index=False)
            print('все успешно объединено')

        elif command_union == 2:
            col_files = int(input('Введите кол-во файлов: '))

            files = []

            for col in range(1,col_files):
                a = input('Введите название файла: ')
                files.append(a)

            for file in files:
                df = pd.read_csv(file)

                df3 = pd.concat([df], ignore_index=True)
                df3.to_csv(f'party_new_file_{random.randint(1,201)}.csv', index=False)
                print('все успешно объединено')

        else:
            print('Извините но такого нет')

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

        new_filename = input('Введите новое название файла: ')

        df = pd.read_excel(filename)
        read = df.head(n)
        print(read)

        df1 = pd.DataFrame(read)
        df1.to_csv(f'{new_filename}')

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

            chunk_size = int(input('Введите оптимальный chunk_size: '))

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

    elif convertation_file == 'csv_to_sql':
        input_name_file_csv = input('Введите название файла: ')

        input_name_file_sql = input('Введите название файла: ')

        conn = sqlite3.connect(input_name_file_sql)

        df = pd.read_csv(input_name_file_csv)
        df.to_sql('contact', conn, if_exists='append', index=False)

    elif convertation_file == 'sql_to_csv':
        print('???')


def process_fast_search(filename, search_term):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if search_term in line:
                return line


def converter():
    print('программа converter предназначена для работы с файлами и всякими расширениями')

    extension = input('Введите с каким расширением вы хотите работать (csv, xlsx, txt, con, fast_search): ')

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

    elif extension == 'fast_search':
        filee = input('Введите название файла: ')

        word = input('Введите данные которые хотите найти: ')

        start_time = time.time()

        for files in filee:
            result = process_fast_search(files, word)
            print(result)

            print("--- %s seconds ---" % (time.time() - start_time))

    elif extension == 'quit':
        sys.exit()


def main():
    converter()


if __name__ == '__main__':
    main()