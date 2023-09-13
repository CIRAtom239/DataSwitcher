import pandas as pd
import random


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
            # Ручное разделение

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
            #Автоматическое разделение

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