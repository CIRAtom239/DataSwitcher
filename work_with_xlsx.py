import pandas as pd


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