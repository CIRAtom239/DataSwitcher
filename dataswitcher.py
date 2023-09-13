from work_with_fast_search import process_fast_search
from work_with_convertation import process_conversion
from work_with_xlsx import process_xlsx
from work_with_csv import process_csv
from work_with_txt import process_txt
import time
import sys


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