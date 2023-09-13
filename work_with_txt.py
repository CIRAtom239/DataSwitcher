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